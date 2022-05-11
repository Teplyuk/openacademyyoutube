from datetime import date
from odoo import api, fields, models, _, tools


class YoutubePatient(models.Model):
    _name = "youtube.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Youtube Patient"
    _rec_name = 'name'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    active2 = fields.Boolean(string='Active2', default=True, tracking=True)
    appointment_id = fields.Many2one(string='Appointment', comodel_name='youtube.appointment')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('youtube.patient.tag', string='Tags')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for ref in self:
            # print("today", today)
            # print("date_of_birth.year", ref.date_of_birth)
            if ref.date_of_birth:
                ref.age = today.year - ref.date_of_birth.year
            else:
                ref.age = 0
