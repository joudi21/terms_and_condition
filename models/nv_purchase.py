from ast import literal_eval
from odoo import api, fields, models, _

import logging

# Get the logger
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # note = fields.Text('Terms and Conditions',default=_default_note)
    notes = fields.Text('Terms and Conditions', default=lambda self: self.env['ir.config_parameter'].sudo().get_param('purchase.use_purchase_note') and self.env.user.company_id.purchase_note or '')


    # @api.model
    # def _default_note(self):
    #     return self.env['ir.config_parameter'].sudo().get_param('purchase.use_purchase_note') and self.env.user.company_id.purchase_note or ''
