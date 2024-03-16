from odoo import fields, models

class PosSession(models.Model):
    _inherit='pos.session'

    def _compute_cash_balance(self):
        return super()._compute_cash_balance()

    