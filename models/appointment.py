import random
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

# REFERENCE
# - 1 -
# comodel_name in first position without name or with name
# patient_id = fields.Many2one(string='Patient', comodel_name='youtube.patient')
# OR
# patient_id = fields.Many2one('youtube.patient', string='Patient')

# - 2 -
# ondelete=
# patient_id = fields.Many2one(string='Patient', comodel_name='youtube.patient', ondelete='restrict')
# ondelete='restrict' - запрещет удалять, если есть связь
# ondelete='cascade' - удаляет элемент и все подчиненные

####################################################################################


class YoutubeAppointment(models.Model):
    _name = "youtube.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Youtube Appointment"
    _rec_name = 'patient_id'
    _order = 'patient_id asc'                  # ('patient_id desc')

    patient_id = fields.Many2one(string='Patient', comodel_name='youtube.patient', ondelete='restrict')
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
    pharmacy_lines_ids = fields.One2many('youtube.appointment.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_prices = fields.Boolean(string='Hide sales prices')
    operation_id = fields.Many2one(string='Operation', comodel_name='youtube.operation')
    progress = fields.Integer(string='Progress', compute='_compute_progress')
    duration = fields.Float(string='Duration')

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError(_("You can delete appointment only with 'Draft' status!"))
        return super(YoutubeAppointment, self).unlink()

    # @api.model
    # def create(self, vals_list):            не работает, потому что у нас нет поля 'name' Индус не показывал как создал!
    #     vals_list['name'] = self.env['ir.sequence'].next_by_code('youtube.appointment')
    #     return super(YoutubeAppointment, self).create(vals_list)

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
        action = self.env.ref('openacademy_youtube.action_cancel_appointment').read()[0]
        return action
        # -2-
        # self.state = 'cancel'
        # -1-
        # for rec in self:
        #     rec.state = 'cancel'
        # dict(self._fields['type'].selection).get(self.type)

    def action_tree_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'in_consultation'

    def action_tree_done(self):
        for rec in self:
            rec.state = 'done'

    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'gray':
                progress = random.randrange(0,25)
            elif rec.state == 'draft':
                progress = 50
            elif rec.state == 'in_consultation':
                progress = 75
            elif rec.state == 'done':
                progress = 100
            else:
                progress = 0
            rec.progress = progress


class AppointmentLines(models.Model):
    _name = "youtube.appointment.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('youtube.appointment', string='Appointment')













