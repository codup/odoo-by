# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp import models, fields, api, _

class account_invoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    @api.multi
    def action_bill_sent(self):
        assert len(self) == 1, 'This option should only be used for a single id at a time.'
        template = self.env.ref('l10n_by_doc.email_template_edi_bill', False)
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='account.invoice',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template.id,
            default_composition_mode='comment',
            mark_invoice_as_sent=True,
        )
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }

    @api.multi
    def bill_print(self):
        assert len(self) == 1, 'This option should only be used for a single id at a time.'
        self.sent = True
        return self.env['report'].get_action(self, 'l10n_by_doc.report_bill')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: