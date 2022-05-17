# -*- coding: utf-8 -*-
{
    'name': "OpenAcademyYoutube",
    'summary': """Teplyuk youtube-trainings""",
    'description': """training courses""",
    'author': "DM/Teplyuk",
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
    'depends': ['base', 'mail', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequences_patient.xml',
        'data/patient_data_tag.xml',
        'data/youtube.patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/playground_view.xml',
        'views/patient_tag_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}