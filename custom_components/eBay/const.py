"""Constants for the ebay integration."""
from homeassistant.components.sensor import SensorEntityDescription

DOMAIN = "ebay"
OAUTH2_AUTHORIZE = "https://auth.ebay.com/oauth2/authorize"
OAUTH2_TOKEN = "https://api.ebay.com/identity/v1/oauth2/token"
SCOPES = "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly"
UNFULFILLED_ORDERS_URL = "https://api.ebay.com/sell/fulfillment/v1/order?filter=orderfulfillmentstatus:%7BNOT_STARTED%7CIN_PROGRESS%7D"
SELLER_FUNDS_SUMMARY_URL = "https://apiz.ebay.com/sell/finances/v1/seller_funds_summary"


EBAY_QUERIES_SENSOR: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="ebay_total_unfulfilled_orders",
        name="eBay Total Unfulfilled Orders",
        icon="mdi:package-variant-closed",
    ),
    SensorEntityDescription(
        key="ebay_orders_due_today",
        name="eBay Orders Due Today",
        icon="mdi:package-variant-closed",
    ),
    SensorEntityDescription(
        key="ebay_available_funds",
        name="eBay Available Funds",
        icon="mdi:currency-usd",
        native_unit_of_measurement="USD",
    ),
    SensorEntityDescription(
        key="ebay_funds_on_hold",
        name="eBay Funds on Hold",
        icon="mdi:currency-usd",
        native_unit_of_measurement="USD",
    ),
    SensorEntityDescription(
        key="ebay_processing_funds",
        name="eBay Funds Processing",
        icon="mdi:currency-usd",
        native_unit_of_measurement="USD",
    ),
    SensorEntityDescription(
        key="ebay_total_funds",
        name="eBay Total Funds",
        icon="mdi:currency-usd",
        native_unit_of_measurement="USD",
    ),
)
