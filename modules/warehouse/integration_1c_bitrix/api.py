from integration_1c.api import OneCAPI
from integration_bitrix.api import Bitrix24API

class IntegrationAPI:
    def __init__(self, onec_base_url, onec_token, bitrix_webhook_url):
        self.onec_api = OneCAPI(onec_base_url, onec_token)
        self.bitrix_api = Bitrix24API(bitrix_webhook_url)

    def sync_data(self):
        onec_data = self.onec_api.get_data("orders")
        for order in onec_data:
            self.bitrix_api.call_method("crm.deal.add", {"fields": order})
