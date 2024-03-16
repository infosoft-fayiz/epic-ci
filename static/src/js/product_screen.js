odoo.define('pos_cash_item_restrict.ProductScreen', function(require) {
    'use strict';
    
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registeries = require('point_of_sale.Registries');

    const PosCashItemRestrist = (ProductScreen) =>
        class extends ProductScreen {
            constructor() {
                super(...arguments);
            }
            async _onClickPay() {
                let cur_pos = this.env.pos
                let order = cur_pos.get_order()
                let lines = order.get_orderlines();
                let payment_methods = []
                
                if (order && lines.length > 0){
                    _.each(lines, function (line) {
                        let product = line.get_product();
                        if (product['default_code'].includes('CASHITEM'))
                            payment_methods = cur_pos['payment_methods']; 
                             
                    })
                }
            super._onClickPay();
            }
        };

    Registeries.Component.extend(ProductScreen, PosCashItemRestrist);

    return ProductScreen;
});