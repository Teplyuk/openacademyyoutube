
from odoo import api, fields, models, _, tools

# REFERENCE
# - 1 -
# comodel_name in first position without name or with name
# patient_id = fields.Many2one(string='Patient', comodel_name='youtube.patient')
# OR
# patient_id = fields.Many2one('youtube.patient', string='Patient')

####################################################################################

class YoutubeAppointment(models.Model):
    _name = "youtube.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Youtube Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(string='Patient', comodel_name='youtube.patient')
    gender = fields.Selection(related='patient_id.gender', help='Sex')              #readonly=False
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help='Комментарий')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection(
        [('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High'), ('4', 'Very Very High'), ('5', 'Absolut')],
        string='Priority', tracking=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancel'), ('gray', 'Gray')],
        string='Status', tracking=True, default='draft', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def object_button(self):
        message = 'Hello World!'
        print(message)
        return {
            'effect': {
                'fadeout': 'slow',
                'message': message,
                'img_url': '/web/static/img/smiling_face.svg',
                'type': 'rainbow_man',
            }
        }

    def cancel_status_button(self):
        self.state = 'cancel'
        # for rec in self:
        #     rec.state = 'cancel'
        # dict(self._fields['type'].selection).get(self.type)
