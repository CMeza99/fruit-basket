# pylint: disable=no-self-use, too-few-public-methods
"""Tests for `fruit_basket` package."""
from collections import Counter
from pathlib import Path

from fruit_basket.main import (
    countbychar,
    oldestfruit,
    readfiledata,
    sumallfruit,
    sumeachfruit,
    totaltypes,
)


class TestFruitBasket:
    """Tests for `fruit_basket` package."""

    def test_fruit_basket_main_000(self):
        """First test run."""
        result = readfiledata(Path(__file__).parent.joinpath("data", "given.csv"))
        assert totaltypes(result) == 5
        assert sumallfruit(result) == 22
        assert sumeachfruit(result)["apple"] == 5
        assert sumeachfruit(result)["orange"] == 6
        assert oldestfruit(result) == ({"pineapple", "orange"}, 6)
        assert countbychar(result)["apple"] == Counter(
            {("red", "sweet"): 3, ("yellow", "sweet"): 1, ("green", "tart"): 1},
        )
