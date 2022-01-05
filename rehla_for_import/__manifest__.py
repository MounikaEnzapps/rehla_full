{
    'name': "Rehla Import",
    'author':
        'ENZAPPS',
    'summary': """
This module is for My School Managment.
""",

    'description': """
        This module is for My School Managment.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base','sale_management','stock', 'purchase','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_payment_partner','account_invoice_import_ubl','account_invoice_ubl',],
    "images": ['static/description/icon.png'],
    'data': [
        # 'security/contact_form.xml',
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        # 'data/sequence.xml',
        # 'wizards/create_address.xml',
        # 'views/image.xml',
        # 'views/product.xml',
        'views/sale.xml',



        # 'views/newxml.xml',


    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
