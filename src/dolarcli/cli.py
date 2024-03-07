"""dolarcli CLI."""

from math import ceil
import typer
from dolarcli.core.dolar_api import DolarAPIImpl
from dolarcli.presentation.formatters import CurrencyTyperPrinter

app = typer.Typer()


@app.command()
def blue(quote_type: str = "") -> None:
    """Gives a dolar blue live cotization"""
    dolar_api = DolarAPIImpl(currency_type=quote_type)
    currency_quote = dolar_api.get_now_currency_quote()
    printer = CurrencyTyperPrinter()
    printer.print_instant(currency_quote=currency_quote)

@app.command()
def conversion_pesos(pesos: int, custom_cotization: float = None) -> None:
    """Gives a convertion of an amount in pesos in dolars"""
    dolar_value = custom_cotization
    if not dolar_value:
        dolar_api = DolarAPIImpl(currency_type="blue")
        currency_quote = dolar_api.get_now_currency_quote()
        dolar_value = (currency_quote.buy_value + currency_quote.sell_value) / 2
    amount_in_uds = ceil((pesos / dolar_value)/100) *100
    remaining = float(amount_in_uds) - float(pesos / dolar_value)
    typer.echo(f"Cotización Dolar: {dolar_value}")
    typer.echo(f"Cantidad en uds: {float(pesos / dolar_value)}")
    typer.echo(f"Hay que vender {ceil(amount_in_uds)} y sobran {int(remaining * dolar_value)} pesos")

if __name__ == "__main__":
    app()
