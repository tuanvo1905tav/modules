# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Total(models.Model):
    _name = 'totals'
    _description = 'Total'

    name = fields.Char('Name', required=True)
    tong_tien = fields.Float('Tong tien')
    tong_so_luong = fields.Integer('Tong so luong')



