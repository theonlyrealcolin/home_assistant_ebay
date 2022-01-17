from datetime import timedelta
import logging

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)


from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from .const import DOMAIN, EBAY_QUERIES_SENSOR
from .api import get_ebay_data

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    # assuming API object stored here by __init__.py
    api = hass.data[DOMAIN][entry.entry_id]

    async def async_update_data():
        try:
            await api.session.async_ensure_token_valid(),
            access_token = api.session.token["access_token"]
            return await get_ebay_data(access_token)
        except Exception as ex:
            raise UpdateFailed(f"Error getting Ebay data: {ex}") from ex

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        # Name of the data. For logging purposes.
        name="ebay",
        update_method=async_update_data,
        # Polling interval. Will only be polled if there are subscribers.
        update_interval=timedelta(seconds=10),
    )
    await coordinator.async_config_entry_first_refresh()

    ebay_entity_list = []

    ebay_entity_list.extend(
        [
            ebayOrders(
                coordinator,
                description,
            )
            for description in EBAY_QUERIES_SENSOR
        ]
    )

    if ebay_entity_list:
        async_add_entities(ebay_entity_list)


class ebayOrders(CoordinatorEntity, SensorEntity):
    """An entity using CoordinatorEntity."""

    def __init__(self, coordinator, description: SensorEntityDescription):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{description.key}"

    @property
    def native_value(self):
        """Value of sensor."""
        return self.coordinator.data[self.entity_description.key]
