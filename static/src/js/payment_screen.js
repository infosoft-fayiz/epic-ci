
odoo.define('pos_cash_item.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const Dialog = require('web.Dialog')

    const PosCashItem = (PaymentScreen) =>
        class extends PaymentScreen {
            async validateOrder(isForceValidate) {
                let order_lines = this.env.pos.get_order().get_orderlines()
                let payment_lines = this.env.pos.get_order().get_paymentlines()

                    _.each(order_lines, function (line) {
                        let product = line.get_product()
                        // if (product['default_code'].includes('CASHITEM')){
                            if (payment_lines['0']['name'] !== 'Cash'){
                                Dialog.alert(this, 'Error');
                                return;
                            // }
                        }
                    })

                return super.validateOrder(isForceValidate);
            }
        };

    Registries.Component.extend(PaymentScreen, PosCashItem);

    return PaymentScreen;
});
