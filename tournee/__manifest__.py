# -*- coding: utf-8 -*-
{
    'name': "Tournées",
    'summary': """ Tournées
        """,
    'description': """
        Tournées
    """,
    'author': "SYENTYS",
    'website': "http://www.syentys.com",
    'version': '15.0.1.0.0',
    
    'depends': [
        'base', 'contacts', 'industry_fsm', 'hr', 'mail', 'cna_base', 'barcodes', 'documents',
        'project', 'web_tree_dynamic_colored_field', 'web', 'documents_project', 'hr_timesheet', 'utm'],

    'data': [
        # Security
        'security/tags_security.xml',
        'security/ir.model.access.csv',

        # data
        'data/tags_sequence.xml',
        'data/mail_template.xml',

        # wizard
        'wizard/add_tags_wizard.xml',
        'wizard/add_comment_task.xml',

        # views
        'views/anomalie_views.xml',
        'views/tags_views.xml',
        'views/tourne_views.xml',
        'views/menu.xml',

        # report
        'report/report_views.xml',
        'report/tags_template.xml',
    ],
    'assets': {
            'web.assets_qweb': ["tournee/static/src/xml/paperclip_attachment.xml"],
    },
    'installable': True,
}
