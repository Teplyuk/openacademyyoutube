
from odoo import api, fields, models, _


class PatientTag(models.Model):
    _name = "youtube.patient.tag"
    _description = "Youtube Patient Tag"

    name = fields.Char(string='Name', required=True, trim=False)     #trim - отключает функцию 1С СокрЛП() (удаление пробелов лишних)
    active = fields.Boolean(string='Active', default=True, copy=False)
    color = fields.Integer(string='Color')
    color_hex = fields.Char(string='Color HEX')
    sequence = fields.Integer(string='Sequence')

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)") % (self.name)
        default['sequence'] = 10
        return super(PatientTag, self).copy(default)

    _sql_constraints = [
        ('name_unique_tag',
         'UNIQUE(name, active)',
         "The Tag title must be unique"),

        ('check_sequence',
         'CHECK(sequence > 0)',
         "Sequence must be non zero positive number"),
    ]

