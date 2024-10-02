# -*- coding: utf-8 -*-
{
    'name': 'My Invoice',
    'version': '16.0.1.0.0',
    'summary': """ My Invoice Custom Template """,
    'author': 'Tasin Tarek',
    'website': '',
    'category': 'Tools',
    'depends': ['base', 'web', 'account'],
    'data': [
        ## Views
        'views/account_move_view.xml',

        ## Report
        'reports/custom_external_layout_standard.xml',
        'reports/custom_account_invoice_report_template.xml',
        'reports/custom_account_invoice_report.xml',
    ],'assets': {
            'web.assets_backend': [
                # 'my_invoice/static/src/**/*'
            ],
        },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
