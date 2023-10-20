from odoo import models, fields, api
from validators import url as validate_url


class ResPartner(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char(string="Facebook URL", icon="fa-facebook")
    linkedin_url = fields.Char(string="LinkedIn URL", icon="fa-linkedin")
    twitter_url = fields.Char(string="Twitter URL", icon="fa-twitter")
    is_complete_profile = fields.Boolean("Complete Profile", compute='_compute_is_complete_profile', store=True)

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url')
    def _compute_is_complete_profile(self):
        for record in self:
            record.is_complete_profile = True
            if not record.facebook_url or not record.linkedin_url or not record.twitter_url:
                record.is_complete_profile = False

    @api.constrains('facebook_url', 'linkedin_url', 'twitter_url')
    def _check_url(self):
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
