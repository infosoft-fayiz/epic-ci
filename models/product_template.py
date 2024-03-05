from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cash_item = fields.Boolean("Cash Item")


class PosSession(models.Model):
    _inherit='pos.session'

    def _loader_params_product_info(self):
        return {
            'search_params': {
                'fields':['cash_item']
            }
        }

    def _get_pos_product_info(self, params):
        return self.env['product.template'].search_read(**params['search_params'])