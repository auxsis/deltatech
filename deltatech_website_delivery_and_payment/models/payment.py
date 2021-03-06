# ©  2015-2020 Deltatech
# See README.rst file on addons root folder for license details


import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    value_limit = fields.Float()
    restrict_label_ids = fields.Many2many("res.partner.category")
