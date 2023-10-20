from odoo import http
from odoo.http import request


class CustomerController(http.Controller):

    @http.route('/customers', type='http', website=True, auth='public')
    def customer_page(self, **kwargs):
        customers = request.env['res.partner'].sudo().search([])
        return request.render('ae_crm_ext_social_networks.customer_page', {
            'customers': customers,
        })

    @http.route('/search/customers', type='json', auth='public', website=True)
    def search_customers(self, search_text):
        customers = request.env['res.partner'].sudo().search([
            '|', ('name', 'ilike', search_text), ('social_accounts', 'ilike', search_text)
        ])
        customer_data = [{'name': customer.name, 'social_accounts': customer.social_accounts} for customer in customers]
        return customer_data