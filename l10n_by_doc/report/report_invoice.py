# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp.osv import osv
from report_helper import QWebHelper

class ByInvoiceReport(osv.AbstractModel):
    _name = 'report.l10n_by_doc.report_invoice'
    def render_html(self, cr, uid, ids, data=None, context=None):
        report_obj = self.pool['report']
        report = report_obj._get_report_from_name(
            cr, uid, 'l10n_by_doc.report_invoice'
        )
        docargs = {
            'helper': QWebHelper(),
            'doc_ids': ids,
            'doc_model': report.model,
            'docs': self.pool[report.model].browse(
                cr, uid, ids, context=context
            ),
        }
        return report_obj.render(
            cr, uid, ids, 'l10n_by_doc.report_invoice',
            docargs, context=context
        )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: