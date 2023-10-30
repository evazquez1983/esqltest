from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        self.partner_model = self.env['res.partner']

    def test_complete_profile(self):
        # Crea un socio con todas las URL de redes sociales y verifica que el campo is_complete_profile sea True.
        partner = self.partner_model.create({
            'name': 'John Doe',
            'facebook_url': 'https://www.facebook.com/johndoe',
            'linkedin_url': 'https://www.linkedin.com/in/johndoe',
            'twitter_url': 'https://twitter.com/johndoe'
        })
        self.assertTrue(partner.is_complete_profile)

    def test_incomplete_profile(self):
        # Crea un socio con una URL de red social faltante y verifica que el campo is_complete_profile sea False.
        partner = self.partner_model.create({
            'name': 'Jane Smith',
            'facebook_url': 'https://www.facebook.com/janesmith',
            'linkedin_url': 'https://www.linkedin.com/in/janesmith'
        })
        self.assertFalse(partner.is_complete_profile)

    def test_invalid_url(self):
        # Intenta crear un socio con una URL de red social no válida y verifica que se genere una excepción.
        with self.assertRaises(models.ValidationError):
            self.partner_model.create({
                'name': 'Bob Johnson',
                'facebook_url': 'https://www.facebook.com/bobjohnson',
                'linkedin_url': 'https://www.linkedin.com/in/bobjohnson',
                'twitter_url': 'invalid_url'
            })