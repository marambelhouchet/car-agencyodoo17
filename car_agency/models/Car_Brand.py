from odoo import models, fields

class CarBrand(models.Model):
    _name = 'car_brand'
    _description = 'Car Brand'

    name = fields.Char(string='Brand Name', required=True)
    image = fields.Binary(string='Brand Image')
    description = fields.Text(string='Description')
    agency_id = fields.Many2one('car_agency', string='Agency', required=True)
