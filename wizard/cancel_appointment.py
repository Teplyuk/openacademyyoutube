
from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = "youtube.cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('youtube.appointment', string='Appointment')
    reason = fields.Text(string='Reason')

    def action_cancel(self):
        return
