# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016-2018 CodUP (<http://codup.com>).
#
##############################################################################

{
    'name': 'Belarus - Documents',
    'version': '1.6',
    'summary': 'Первичные документы',
    'description': """
The module for print documents in accordance laws of Belarus.
============================================================
Возможности:
    * Счет-протокол
    * Счет-фактура
    * Акт выполненных работ
    * Товарная накладная
    * Товарно-транспортная накладная
    """,
    'author': 'CodUP',
    'website': 'http://codup.com',
    'category': 'Localization',
    'sequence': 0,
    'depends': ['sale'],
    'demo': [],
    'data': [
        'data/l10n_by_doc_data.xml',
        'views/account_invoice_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_users_view.xml',
        'report/l10n_by_doc_report.xml',
        'report/report_order.xml',
        'report/report_invoice.xml',
        'report/report_bill.xml',
        'report/report_waybill.xml',
        'report/report_act.xml',
        'data/bill_action_data.xml',
    ],
    'css': ['static/src/css/l10n_by_doc.css'],
    'installable': True,
}
