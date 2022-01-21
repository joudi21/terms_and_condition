from ast import literal_eval
from odoo import api, fields, models

import logging

# Get the logger
_logger = logging.getLogger(__name__)


class NvResCompanyclass(models.Model):
    _inherit = 'res.company'
    purchase_note = fields.Text(string='Default Terms & Conditions', translate=True)