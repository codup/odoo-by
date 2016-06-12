# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from openerp import api, models, fields

class res_users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    print_facsimile = fields.Boolean('Print Facsimile', related='company_id.print_facsimile')
    facsimile = fields.Binary("Facsimile")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: