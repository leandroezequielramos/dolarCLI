import abc
from dolarcli.models.currency_quote import CurrencyQuote
from datetime import datetime, timezone
import requests


class DolarAPI(abc.ABC):

    @abc.abstractmethod
    def get_now_currency_quote(self) -> CurrencyQuote:
        return None


class DolarAPIImpl(DolarAPI):

    def __init__(self, currency_type: str):
        self._uri = "https://dolarapi.com/v1/dolares/blue"
        self._currency_type = currency_type

    def get_now_currency_quote(self) -> CurrencyQuote:
        response = requests.get(self._uri)
        response.raise_for_status()
        return CurrencyQuote(
            sell_value=float(response.json()["venta"]),
            buy_value=float(response.json()["compra"]),
            last_update=datetime.fromisoformat(
                response.json()["fechaActualizacion"][:-1]
            ).replace(tzinfo=timezone.utc),
        )
