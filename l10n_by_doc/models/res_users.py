# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016-2018 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models

class Users(models.Model):
    _inherit = 'res.users'

    print_facsimile = fields.Boolean('Print Facsimile', related='company_id.print_facsimile')
    facsimile = fields.Binary("Facsimile")
