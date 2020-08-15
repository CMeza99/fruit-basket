# pylint: disable=no-self-use, too-few-public-methods
"""Tests for `fruit_basket` package."""
from collections import Counter
from pathlib import Path
from pprint import pprint

from fruit_basket.main import FruitBasket, report


class TestFruitBasket:
    """Tests for `fruit_basket` package."""

    def test_fruit_basket_main_000(self):
        """First test run."""
        basket = FruitBasket(Path(__file__).parent.joinpath("data", "given.csv"))
        print("Inventory Data:")
        pprint(dict(basket.inventory))
        assert basket.total_fruittypes == 5
        assert basket.total_fruits == 22
        for k, v in {"apple": 5, "orange": 6}.items():
            assert basket.totals_byfruit[k] == v
        assert basket.oldestfruits == ({"pineapple", "orange"}, 6)
        assert basket.totals_bychar["apple"] == Counter(
            {("red", "sweet"): 3, ("yellow", "sweet"): 1, ("green", "tart"): 1},
        )
