from decimal import Decimal

from parser.price_parser import parse_eur_prices


def test_parse_eur_prices_supports_comma_decimal():
    assert parse_eur_prices("Milk 1,29 € and bread 0.99 EUR") == [Decimal("1.29"), Decimal("0.99")]


def test_parse_eur_prices_ignores_unlabelled_numbers():
    assert parse_eur_prices("1 kg milk, price unknown") == []
