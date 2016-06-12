# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp import api, models, fields

class res_company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    unp = fields.Char('UNP', related='partner_id.unp')
    okpo = fields.Char('OKPO', related='partner_id.okpo')
    chief_id = fields.Many2one('res.users', 'Chief')
    accountant_id = fields.Many2one('res.users', 'General Accountant')
    print_facsimile = fields.Boolean('Print Facsimile', help="Check this for adding Facsimiles of responsible persons to documents.")
    print_stamp = fields.Boolean('Print Stamp', help="Check this for adding Stamp of company to documents.")
    stamp = fields.Binary('Stamp')
    print_anywhere = fields.Boolean('Print Anywhere', default=True, help="Uncheck this, if you want add Facsimile and Stamp only in email.")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: