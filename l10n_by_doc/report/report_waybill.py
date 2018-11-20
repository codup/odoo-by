# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016-2018 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, models
from odoo.addons.l10n_by_doc.report.report_helper import QWebHelper

class ByWayBillReport(models.AbstractModel):
    _name = 'report.l10n_by_doc.report_waybill'

    @api.multi
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.invoice'].browse(docids)
        return {
            'helper': QWebHelper(),
            'doc_ids': docs.ids,
            'doc_model': 'account.invoice',
            'docs': docs
        }
