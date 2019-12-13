{
    'name': 'TMC Partner Customizations',
    'summary': 'Add or hide some information related to partner',
    'version': '13.0.1.0.0',
    'category': 'Contacts',
    'website': 'https://www.tmcrosario.gob.ar',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [
        # 'partner_contact_birthdate',
        # 'partner_contact_gender',
        'partner_firstname',
        'base_address_extended',
        'partner_fiscal',
        'partner_municipal'
    ],
    'data': [
        'views/partner.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'qweb': [],
}  # yapf: disable
