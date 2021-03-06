# -*- coding: utf-8 -*-

from odoo import models, fields, api

class test(models.Model):
    _name = 'test.test'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    test = fields.Char('test')

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100