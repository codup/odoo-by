# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp.osv import fields, osv

class sale_order(osv.osv):
    _name = 'sale.order'
    _inherit = 'sale.order'

    def print_quotation(self, cr, uid, ids, context=None):
        '''
        This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        self.signal_workflow(cr, uid, ids, 'quotation_sent')
        return self.pool['report'].get_action(cr, uid, ids, 'l10n_by_doc.report_order', context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: