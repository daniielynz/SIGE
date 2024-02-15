{
    'name': 'Módulo de gestión de notas',
    'summary': 'Módulo para realizar la gestión de notas y alumnos.',
    'description': 'Este módulo puede ser utilizado por alumnos, maestros y padres para visualizar y gestionar las notas de los alumnos en sus actividades.',
    'version': '1.0.0',
    'category': 'Human Resources',
    'author': 'Christofer Borrayo',
    'data': [
        'security/groups.xml',
        'security/alumnado.xml',
        'security/practicas.xml',
        'security/tutoriafct.xml',
        'security/empresa.xml',

        'views/menu_principal.xml',

        'views/alumnado/form_view.xml',
        'views/alumnado/tree_view.xml',
        'views/alumnado/menu_alumnado.xml',

        'views/practicas/form_view.xml',
        'views/practicas/tree_view.xml',
        'views/practicas/menu_practicas.xml',

        'views/tutoria/form_view.xml',
        'views/tutoria/tree_view.xml',
        'views/tutoria/menu_tutoria.xml',

        'views/empresa/form_view.xml',
        'views/empresa/tree_view.xml',
        'views/empresa/menu_empresa.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}