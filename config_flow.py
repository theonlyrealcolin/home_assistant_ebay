"""Config flow for ebay."""
import logging
from .const import DOMAIN
from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.core import HomeAssistant, callback


from yarl import URL
import jwt
import secrets

DATA_JWT_SECRET = "oauth2_jwt_secret"


class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow to handle ebay OAuth2 authentication."""

    DOMAIN = DOMAIN
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    async def async_oauth_create_entry(self, data: dict) -> dict:
        """Create an entry for the flow.
        Ok to override if you want to fetch extra info or even add another step.
        """
        return self.async_create_entry(title=DOMAIN, data=data)

    async def async_step_user(self, user_input=None):
        """Handle a flow start."""
        if self.hass.config_entries.async_entries(DOMAIN):
            return self.async_abort(reason="already_setup")

        return await super().async_step_user(user_input)
