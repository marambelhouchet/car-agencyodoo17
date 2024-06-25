from odoo import models, fields

class CarAgency(models.Model):
    _name = 'car_agency'
    _description = 'Car Agency'

    name = fields.Char(required=True)
    responsible_id = fields.Many2one('res.partner', string='Responsible', required=True)
    car_ids = fields.One2many('car', 'agency_id', string='Cars')

    def action_view_brands(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Car Brands',
            'view_mode': 'tree,form',
            'res_model': 'car_brand',
            'domain': [('agency_id', '=', self.id)],
            'context': "{'create': False}"
        }
