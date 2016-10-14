# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2016 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    unp = fields.Char('UNP')
    okpo = fields.Char('OKPO')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: