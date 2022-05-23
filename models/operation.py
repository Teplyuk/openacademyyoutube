
from odoo import api, fields, models, _


class YoutubeOperation(models.Model):
    _name = "youtube.operation"
    _description = "Youtube Operation"
    _log_access = False

    doctor_id = fields.Many2one(string='Doctor', comodel_name='res.users')
    operation_name = fields.Char(string='Name')

    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]
