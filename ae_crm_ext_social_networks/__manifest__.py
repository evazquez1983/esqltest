{
    'name': "ae_crm_ext_social_networks",
    'summary': """ 
        Allows registering the url of the following social accounts for each customer.""",

    'author': "Esequiel Tamayo Vazquez",
    'category': "Sales/CRM",
    'version': '16.0.0.0.0',
    'license': 'LGPL-3',
    'depends': ['base', 'portal', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/view_partner_form.xml',
        'views/view_partner_tree.xml',
        'views/view_partner_filter.xml',
        'views/template_partner.xml',
    ],
}
