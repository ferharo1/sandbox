# -*- coding: utf-8 -*-
{
    'name': "Construction 4.0",

    'summary': """
        Construction features for Odoo 11""",

    'description': """
        This module include some new features
    """,

    'author': "Directiva Digital",
    'website': "http://www.directivadigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}