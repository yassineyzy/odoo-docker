# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="gender")
    identity = fields.Integer('ID')
    adress = fields.Text('adress')
    subscribe_date = fields.Datetime()
    email = fields.Char('email')
    phone = fields.Integer(string="phone number")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
