# -*- coding: utf-8 -*-
{
    'name': "Hospital Americain Base",
    'summary': """ Hospital Americain Base
        """,
    'description': """
        Hospital Americain Base
    """,
    'author': "SYENTYS",
    'website': "http://www.syentys.com",
    'version': '15.0.1.0.0',
    'depends': [
        'base', 'contacts', 'industry_fsm', 'hr', 'mail', 'web', 'report_xlsx'
    ],
    'data': [
        # security
        'security/activities_security.xml',
        'security/ir.model.access.csv',

        # views
        'views/model_importance_views.xml',
        'views/res_partner_views.xml',
        'views/site_lieu_views.xml',
        'views/site_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
}
