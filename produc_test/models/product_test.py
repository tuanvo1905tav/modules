from odoo import fields, models, api


class ProductTest(models.Model):
    _name = 'product.test'
    _description = 'Description'

    name = fields.Char('Name', required=True)
    amount = fields.Integer('Amount')
    price = fields.Float('Price')
