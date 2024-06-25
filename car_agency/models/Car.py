from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Car(models.Model):
    _name = 'car'
    _description = 'Car'

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
    customer_id = fields.Many2one('res.partner', string='Customer')
    note = fields.Text(string='Damage Note')

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for record in self:
            if len(record.registration_number) != 8 or not record.registration_number.isdigit() or int(
                    record.registration_number) <= 0:
                raise ValidationError('The registration number must be a positive integer with exactly 8 digits.')
