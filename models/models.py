# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP




class ResPartner(models.Model):
    _inherit = 'res.partner'
    _auto = True

    testssss1 = fields.Selection([('semanal','Semanal'),('catorcenal','Catorcenal'),('veintiunodias','21 dias'),('mensual','Mensual')],string='Periodicidad')
    testssss2 = fields.Integer(string='Cantidad')
    testssss3 = fields.Selection([('d1','L - D'),('d2','Sem inicio'),('d3','Sem inicio'),('d4','1 - 3')],string='Dato 1')
    testssss4 = fields.Selection([('d1','X'),('d2','Sem inicio'),('d3','Sem inicio'),('d4','X')],string='Dato 2')

    @api.multi
    def store_my_res_partner_specialdata(self):
    	print "Se llamo aqui"
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100