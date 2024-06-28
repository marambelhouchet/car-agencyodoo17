from odoo import models, fields

class Res(models.Model):
    _name = 'res'

    cin_number = fields.Char(string='CIN Number')
    partner_id = fields.Many2one('res.partner', string='Name')
    email = fields.Char(related='partner_id.email', string='Email', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)
