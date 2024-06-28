from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CarAgency(models.Model):
    _name = 'car_agency'
    _description = 'Car Agency'

    name = fields.Char(required=True)
    responsible_id = fields.Many2one('res.partner', string='Responsible', required=True)
    car_ids = fields.One2many('car', 'agency_id', string='Cars')
    image = fields.Binary(string='Agency Image')
    brand_count = fields.Integer(string='Number of Brands', compute='_compute_brand_count')

    @api.depends('car_ids')
    def _compute_brand_count(self):
        for agency in self:
            agency.brand_count = self.env['car_brand'].search_count([('agency_id', '=', agency.id)])

    def action_view_brands(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'Car Brands ({self.brand_count} Brands)',
            'view_mode': 'tree,form',
            'res_model': 'car_brand',
            'domain': [('agency_id', '=', self.id)],
            'context': {'create': False},
        }
