from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cash_item = fields.Boolean("Cash Item")

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('cash_item')
        return result

    # def _loader_params_product_product(self):
    #     return {
    #         'search_params': {
    #             'fields':['cash_item']
    #         }
    #     }

    
    # def _get_pos_product_info(self, params):
    #     return self.env['product.template'].search_read(**params['search_params'])