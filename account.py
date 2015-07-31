'''
Created on 30-jul.-2015

@author: stijn
'''
from datetime import datetime, timedelta
import time
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from openerp import workflow
from unittest.util import _ordered_count

class AccountInvoice(osv.Model):
    _inherit = 'account.invoice'
        
    def _compute_amount(self):
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line),
        self.amount_tax = sum(line.amount for line in self.tax_line),
        self.amount_total = (self.amount_untaxed ) * (1 + self.xx_insurance_percentage /100) + self.amount_tax,
     

    _columns = {
            'xx_insurance_method' : fields.many2one('xx.insurance.method',string='Insurance method'),
            'xx_insurance_percentage' : fields.float(string="Insurance percentage"),
            'xx_insurance_cost' : fields.float(string="Insurance Cost")
              
    }