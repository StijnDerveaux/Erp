# -*- coding: utf-8 -*-
{
    #naam aangepast naar mijn naam
	'name' : 'KH Leuven',
    'version' : '0.1',
    'author' : 'Stijn Derveaux',
    'category' : 'KH Leuven',
    'description' : """
""",
    'depends' : ['sale', 'stock', 'account', 'website_sale'],
    'data': [
        'view/sale.xml',
        'view/picking.xml',
        'view/warranty.xml',
        'view/website_sale_templates.xml',
        'view/account.xml',
        #account.xml toegevoegd
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
