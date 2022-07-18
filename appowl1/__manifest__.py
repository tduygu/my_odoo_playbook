# -*- coding: utf-8 -*-
{
    'name': "App Owl 1",

    'summary': """
        An owl sample""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Duygu Tuncay",
    'website': "http://www.duygutuncay.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Samples',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/appowl_book.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/appowl1/static/src/js/component.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
