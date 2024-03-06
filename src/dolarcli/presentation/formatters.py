from abc import ABC, abstractmethod
from datetime import timezone
from dolarcli.models.currency_quote import CurrencyQuote
import typer


class CurrencyPrinter(ABC):

    @abstractmethod
    def print_instant(currency_quote: CurrencyQuote):
        pass


class CurrencyTyperPrinter(CurrencyPrinter):

    def print_instant(self, currency_quote: CurrencyQuote):
        typer.echo("Cotización Dolar Blue")
        typer.echo("=====================")
        typer.echo(f"Ultima actualización: {currency_quote.last_update}")
        typer.echo(f"Venta: {int(currency_quote.sell_value)}")
        typer.echo(f"Compra: {int(currency_quote.buy_value)}")
        typer.echo(
            f"Promedio: {int((currency_quote.buy_value + currency_quote.sell_value)/ 2)}"
        )
