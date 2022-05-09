# -*- coding: utf-8 -*-
{
    'name': "OpenAcademyYoutube",
    'summary': """Teplyuk youtube-trainings""",
    'description': """training courses""",
    'author': "44",
    'website': "",
    'category': 'Administration',
    'version': '1.0.1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
    'sequence': -100,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}