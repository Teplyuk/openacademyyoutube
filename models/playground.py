from odoo import api, fields, models, _, tools
from odoo.tools.safe_eval import safe_eval


class YoutubePlayGround(models.Model):
    _name = "youtube.playground"
    _description = "Youtube PlayGround"

    DEFAULT_NAME_VARIABLES = """Main menu:
       #   env: Odoo Environment on which the action is triggered
       #   model: Odoo Model of the record on which the action is triggered; is a void recordset
       #   record: record on which the action is triggered; may be be void
       #   records: recordset of all records on which the action is triggered in multi mode; may be void
       #   time, datetime, dateutil, timezone: useful Python libraries
       #  log(message, level='info'):logging function to record debug information in ir.logging table
       #   UserError: Warning Exception to use with raise
       #   To return an action, assign: action = {...}"""

    model_id = fields.Many2one('ir.model', string='Model')
    code = fields.Text(string='Code', default=DEFAULT_NAME_VARIABLES)
    result = fields.Text(string='Result')

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(), {'self': model})
        except Exception as e:
            self.result = str(e)



    
    