

odoo.define('pos_cash_item_restrict.ProductScreen', function(require) {
    'use strict';
    
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registeries = require('point_of_sale.Registries');
    const {cashItemFlag} = require('epic-pos-dev')

    const PosCashItemRestrist = (ProductScreen) =>
        class extends ProductScreen {
            constructor() {
                super(...arguments);
            }
            async _onClickPay() {
                let order = this.env.pos.get_order()
                let lines = order.get_orderlines();
                
                if (order && lines.length > 0){
                    _.each(lines, function (line) {
                        if (line.product.default_code.includes('CI')){
                            cashItemFlag.cash_item_flag = true;
                            // session = session.filter(
                            //     (method)=>method.id==1
                            // )                         
                        }
                    })
                }
            super._onClickPay();
            }
        };

    Registeries.Component.extend(ProductScreen, PosCashItemRestrist);

    return ProductScreen;
});