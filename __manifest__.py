# -*- coding: utf-8 -*-
{
    'name': "epic-pos-ci",

    'summary': "POS Cash Items module",

    'description': """
        POS module to restirct payment methods for items defined as Cash Items.
    """,

    'author': "Fayiz Asad",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ci_product_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'epic-pos-ci/static/src/js/payment_screen.js',
            # 'epic-pos-ci/static/src/xml/product_screen.xml'
        ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True
}
