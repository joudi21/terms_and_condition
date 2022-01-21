from ast import literal_eval
from odoo import api, fields, models

import logging

# Get the logger
_logger = logging.getLogger(__name__)


class NvResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    purchase_note = fields.Text(related='company_id.purchase_note', string="Terms and Conditions", readonly=False)
    use_purchase_note = fields.Boolean(
        string='Default Terms & Conditions',
        oldname='default_use_purchase_note',
        config_parameter='purchase.use_purchase_note')