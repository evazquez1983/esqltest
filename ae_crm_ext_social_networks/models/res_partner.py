from odoo import models, fields, api
from validators import url as validate_url


class ResPartner(models.Model):
    """
    Modelo personalizado que extiende res.partner para agregar campos de URL de redes sociales.

    Campos adicionales:
    - facebook_url: URL de Facebook del socio.
    - linkedin_url: URL de LinkedIn del socio.
    - twitter_url: URL de Twitter del socio.
    - is_complete_profile: Indica si el perfil del socio está completo (tiene todas las URL de redes sociales).

    Restricciones:
    - Las URL de Facebook, LinkedIn y Twitter deben ser válidas.

    """

    _inherit = 'res.partner'

    facebook_url = fields.Char(string="Facebook URL", icon="fa-facebook")
    linkedin_url = fields.Char(string="LinkedIn URL", icon="fa-linkedin")
    twitter_url = fields.Char(string="Twitter URL", icon="fa-twitter")
    is_complete_profile = fields.Boolean("Complete Profile", compute='_compute_is_complete_profile', store=True)

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url')
    def _compute_is_complete_profile(self):
        """
        Calcula el valor del campo is_complete_profile en función de las URL de redes sociales.

        Si todas las URL de redes sociales están presentes, se establece en True. De lo contrario, se establece en False.

        """
        for record in self:
            record.is_complete_profile = True
            if not record.facebook_url or not record.linkedin_url or not record.twitter_url:
                record.is_complete_profile = False

    @api.constrains('facebook_url', 'linkedin_url', 'twitter_url')
    def _check_url(self):
        """
        Verifica que las URL de Facebook, LinkedIn y Twitter sean válidas.

        Si alguna URL no es válida, se genera una excepción de validación.

        """
        for record in self:
            if record.facebook_url:
                if 'facebook' in record.facebook_url:
                    if not validate_url(record.facebook_url):
                        raise models.ValidationError('La URL ingresada no es válida.')

            if record.linkedin_url:
                if 'linkedin' in record.linkedin_url:
                    if not validate_url(record.linkedin_url):
                        raise models.ValidationError('La URL ingresada no es válida.')

            if record.twitter_url:
                if 'twitter' in record.twitter_url:
                    if not validate_url(record.twitter_url):
                        raise models.ValidationError('La URL ingresada no es válida.')