
from odoo import api, fields, models, _


class YoutubeOperation(models.Model):
    _name = "youtube.operation"
    _description = "Youtube Operation"
    _log_access = False

    doctor_id = fields.Many2one(string='Doctor', comodel_name='res.users')
    operation_name = fields.Char(string='Name')
    reference_record = fields.Reference([('youtube.patient', 'Patient')], string='Record')
    resource_ref = fields.Reference(string='Record reference', selection='_selection_target_model')

    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]

    @api.model
    def _selection_target_model(self):
        return [(model.model, model.name) for model in self.env['ir.model'].sudo().search([])]
