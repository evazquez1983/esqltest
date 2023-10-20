odoo.define('ae_crm_ext_social_networks.customer_search', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $(document).ready(function () {
        $('#search_customer_button').click(function () {
            var searchText = $('#search_customer_input').val();
            ajax.jsonRpc('/search/customers', 'call', {
                search_text: searchText,
            }).then(function (result) {
                // Handle the search results
                console.log(result);
            });
        });
    });
});