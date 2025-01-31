{
    'name': 'car_agency',
    'version': '17.0',
    'licence': 'LGPL-3',
    'summary': 'Manage car brands, cars, and agencies in a car rental system.',
    'author': 'maram',
    'depends': ['mail', 'web', 'base'],
    'data': [
        'views/car_brand_views.xml',
        'views/car_views.xml',
        'views/car_agency_views.xml',
        'views/car_agency_menu.xml',
        'views/car_damaged_wizard_views.xml',
        'data/groups.xml',
        'data/access_rights.xml',
        'data/users.xml',
        'views/res.xml',
    ],
    'images': [
        'car_agency/static/description/icon.png',

           ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
