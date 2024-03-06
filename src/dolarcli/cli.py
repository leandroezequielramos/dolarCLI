"""dolarcli CLI."""

import typer
from dolarcli.core.dolar_api import DolarAPIImpl
from dolarcli.presentation.formatters import CurrencyTyperPrinter

app = typer.Typer()


@app.command()
def currency_now(quote_type: str = "") -> None:
    """Say a message."""
    dolar_api = DolarAPIImpl(currency_type=quote_type)
    currency_quote = dolar_api.get_now_currency_quote()
    printer = CurrencyTyperPrinter()
    printer.print_instant(currency_quote=currency_quote)


if __name__ == "__main__":
    app()
