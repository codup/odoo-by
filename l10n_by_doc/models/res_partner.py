# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016-2018 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    unp = fields.Char('UNP')
    okpo = fields.Char('OKPO')
