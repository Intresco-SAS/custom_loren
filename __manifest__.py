# -*- coding: utf-8 -*-
{
    'name': "Módulo-Ferreteria Electricos Loren",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Este modulo modifica el Recibo de la Cocina segun las especificaciones del cliente. 
        Este Recibo se usa para entregar cotizaciones al cliente a través del POS.
        Se usa como base el Modulo de Tiquete de Cocina "pos_kitchen_receipt_app".
    """,

    'author': "Nelson Velez",
    'website': "http://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['pos_kitchen_receipt_app'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'src/templates.xml',
    ],
    'qweb': [
    'static/src/xml/pos.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}