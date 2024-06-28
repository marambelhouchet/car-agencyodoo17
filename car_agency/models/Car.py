from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    cin_number = fields.Char(string='CIN Number')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

class Car(models.Model):
    _name = 'car'
    _description = 'Car'
    _sql_constraints = [
        ('unique_registration_number', 'unique(registration_number)', 'The registration number must be unique.')
    ]

    registration_number = fields.Char(required=True, size=8)
    car_model = fields.Char(required=True)
    mileage = fields.Float()
    status = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('damaged', 'Damaged')
    ], required=True, default='available')
    start_date = fields.Date()
    end_date = fields.Date()
    agency_id = fields.Many2one('car_agency', string='Agency', required=True)
    customer_id = fields.Many2one('res', string='Customer')
    note = fields.Text(string='Damage Note')
    brand_id = fields.Many2one('car_brand', string='Brand', required=True)

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for record in self:
            if len(record.registration_number) != 8 or not record.registration_number.isdigit() or int(record.registration_number) <= 0:
                raise ValidationError('The registration number must be a positive integer with exactly 8 digits.')
