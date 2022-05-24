import datetime
from datetime import date
from dateutil import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = "youtube.cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('youtube.appointment', string='Appointment',)
                                     # domain=[('state', '=', 'draft'), ('priority', 'in', ('0', '1', ''))])
    reason = fields.Text(string='Reason')
    date_cancel = fields.Date(string='Cancellation Date')

    def action_cancel(self):
        # ПЕРВАЯ УДАЧНАЯ ПОПЫТКА РАБОТЫ С ЗАПРОСОМ ЧЕРЕЗ ПИТОН
        # cr = self._cr
        # list_youtube_patient = 'youtube_patient'
        # query = 'select * from ' + list_youtube_patient
        # cr.execute(query)
        # my_answer = cr.fetchall()
        # print(my_answer)
        #
        cancel_day = self.env['ir.config_parameter'].get_param('openacademy_youtube.cancel_days')
        allowed_data = self.appointment_id.booking_date - relativedelta.relativedelta(days=int(cancel_day))
        # if self.appointment_id.booking_date == fields.Date.today():
        if allowed_data < date.today():
            raise ValidationError(_("Sorry, cancellation is not allowed for this booking!"))
        self.appointment_id.state = 'cancel'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }

