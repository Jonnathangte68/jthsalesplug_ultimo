# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP

import psycopg2

import requests




class ResPartner(models.Model):
    _inherit = 'res.partner'

    testssss1 = fields.Selection([('semanal', 'Semanal'),('catorcenal', 'Catorcenal'),('veintiunodias', '21 dias'),('mensual', 'Mensual')],string='Periodicidad')
    testssss2 = fields.Integer(string='Cantidad')
    testssss3 = fields.Selection([('ld', 'L - D'),('sem_inicio', 'Sem Inicio'),('sem_ini', 'Sem inicial'),('unotres', '1 - 3')],string='Dato 1')
    testssss4 = fields.Selection([('x', 'X'),('ld1', 'L - D'),('ld2', 'L - D'),('X', 'X')],string='Dato 2')
    usuario = fields.Integer(string='Usuario')

    def generate_doc(self):
        payload = {'valor_uno': self.testssss1,'valor_dos': int(self.testssss2), 'valor_tres': self.testssss3,'valor_cuatro': self.testssss4,'valor_cinco':self.env.user.id}
        r = requests.get('http://192.168.1.142:3000/prueba-de-html', params=payload)
        #raise Exception(r)

