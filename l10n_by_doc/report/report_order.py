# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016-2018 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, models
from report_helper import QWebHelper

class BySaleOrderReport(models.AbstractModel):
    _name = 'report.l10n_by_doc.report_order'

    @api.model
    def render_html(self, docids, data=None):
        Report = self.env['report']
        report = Report._get_report_from_name('l10n_by_doc.report_order')
        selected_modules = self.env[report.model].browse(docids)
        docargs = {
            'helper': QWebHelper(),
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': selected_modules,
        }
        return Report.render('l10n_by_doc.report_order', docargs)
