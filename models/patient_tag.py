
from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "youtube.patient.tag"
    _description = "Youtube Patient Tag"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    color_hex = fields.Char(string='Color HEX')

