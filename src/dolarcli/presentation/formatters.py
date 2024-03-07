from abc import ABC, abstractmethod
from zoneinfo import ZoneInfo
from dolarcli.models.currency_quote import CurrencyQuote
import typer


class CurrencyPrinter(ABC):

    @abstractmethod
    def print_instant(self, currency_quote: CurrencyQuote):
        pass


class CurrencyTyperPrinter(CurrencyPrinter):

    def print_instant(self, currency_quote: CurrencyQuote):
        last_update = currency_quote.last_update.astimezone(
            tz=ZoneInfo("America/Argentina/Cordoba")
        ).strftime("%d/%m/%y %H:%M:%S")
        typer.echo("Cotización Dolar Blue")
        typer.echo("=====================")
        typer.echo(f"Ultima actualización: {last_update}")
        typer.echo(f"Venta: {int(currency_quote.sell_value)}")
        typer.echo(f"Compra: {int(currency_quote.buy_value)}")
        typer.echo(
            "Promedio: "
            f"{int((currency_quote.buy_value + currency_quote.sell_value)/ 2)}"
        )
