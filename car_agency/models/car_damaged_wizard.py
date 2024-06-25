from odoo import models, fields, api

class CarDamageWizard(models.TransientModel):
    _name = 'car_damaged_wizard'
    _description = 'Car Damage Wizard'

    note = fields.Text(string='Damage Note')

    def save_damage_note_and_close(self):
        car_id = self.env.context.get('active_id')
        car = self.env['car'].browse(car_id)
        car.note = self.note
        car.status = 'damaged'
        return {'type': 'ir.actions.act_window_close'}
