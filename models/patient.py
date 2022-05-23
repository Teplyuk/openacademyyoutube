from datetime import date
from dateutil import relativedelta
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


class YoutubePatient(models.Model):
    _name = "youtube.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Youtube Patient"
    _rec_name = 'name'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_compute_age', search='_search_age', tracking=True)
    ref = fields.Char(string='Reference', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    active2 = fields.Boolean(string='Active2', default=True, tracking=True)
    appointment_id = fields.Many2one(string='Appointment', comodel_name='youtube.appointment')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('youtube.patient.tag', string='Tags')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    appointment_ids = fields.One2many('youtube.appointment', 'patient_id', string="Appointments")
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string='Marital status',
                                      tracking=True)
    partner_name = fields.Char(string='Partner Name')

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['youtube.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You cannot delete a patient with appointments!"))

    @api.model
    def create(self, vals_list):
        # print("Hello world, i`m cr8", vals_list)
        my_next_sequence = self.env['ir.sequence'].next_by_code('youtube.patient')
        if ('ref' in vals_list) and vals_list['ref']:
            vals_list['ref'] = vals_list['ref'] + ' // ' + my_next_sequence
        else:
            vals_list['ref'] = my_next_sequence
        return super(YoutubePatient, self).create(vals_list)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            my_next_sequence = self.env['ir.sequence'].next_by_code('youtube.patient')
            vals['ref'] = my_next_sequence
        return super(YoutubePatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            # print("today", today)
            # print("date_of_birth.year", ref.date_of_birth)
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years = rec.age)

    def _search_age(self, operator, value):
        today = date.today()
        date_of_birth = today - relativedelta.relativedelta(years = value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        return [('date_of_birth', '>=', start_of_year),('date_of_birth', '<=', end_of_year)]

    def action_tree_groupby_test(self):
        print('Test button')

    def action_done(self):
        print('Done button test')

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.id, record.name)) for record in self]