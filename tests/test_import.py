"""Test dolarcli."""

import dolarcli


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(dolarcli.__name__, str)
