# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com
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
    "name": "Deltatech CRM",
    "version": "1.0",
    "author": "Dorin Hongu",
    "website": "",
    "description": """

Functionalitati:
 - Adaugare campuri suplimentare: agent comercial
 - Preluare functionalitati din Odoo9 legate de activitati
   
    """,

    'category': 'Customer Relationship Management',
    "depends": ['deltatech', "crm", "deltatech_mail"],



    "data": ['crm_activity_view.xml',
               'crm_lead_view.xml',
               'security/ir.model.access.csv',
               # 'sale_crm_view.xml',
               'crm_view.xml',
               'data/crm_action_data.xml',

               'report/crm_activity_report_view.xml',
               'wizard/crm_assign_agent_view.xml'
             ],

    "active": False,
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
