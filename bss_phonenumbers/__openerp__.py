# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Bluestar Solutions Sàrl (<http://www.blues2.ch>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    'name': 'Phone Numbers',
    'version': '1.0-1',
    "category" : 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """A module to format phone numbers using google-phonenumbers library.""",
    'author': 'bluestar solutions sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['bss_config'],
    'init_xml': [],
    'update_xml': ['bss_partner_phonenumbers_partner_config_view.xml',
                   'bss_partner_phonenumbers_partner_view.xml'],
    'demo_xml': [],
    'test': ['test/test_partner_phonenumbers.yml'],
    'js': ['static/src/js/resource.js'],
    'qweb': ['static/src/xml/resource.xml'], 
    'installable': True,
    'application': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: