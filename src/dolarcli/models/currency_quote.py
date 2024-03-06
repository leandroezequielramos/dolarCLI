from dataclasses import dataclass
from datetime import datetime


@dataclass
class CurrencyQuote:
    sell_value: float
    buy_value: float
    last_update: datetime
