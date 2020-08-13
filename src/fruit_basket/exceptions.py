"""Exceptions module."""


class FruitBasketError(Exception):
    """Base Exception for Fruit Basket."""

    fmt = "{}"

    def __init__(self, *args, **kwargs):
        msg = self.fmt.format(*args, **kwargs)
        super().__init__(self, msg)
