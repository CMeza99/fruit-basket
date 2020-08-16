"""Main definitions of classes and functions."""
import csv
import logging
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from itertools import chain
from os import PathLike
from pathlib import Path
from typing import Mapping, Sequence, Tuple, Union

from fruit_basket.exceptions import DataError


# Note: Setting compare and hash to false does not prevent attribute from being included in the hash.
@dataclass(eq=True, frozen=True)
class FruitAttributes:
    """Atributes of fruit."""

    # TODO: Investigate stakeholder requirements, should `char` should be a set instead.
    # The current desired output shows characteristics order matter.
    age: field(default=int, compare=False, hash=False)
    char: Tuple[str]


@dataclass
class FruitBasket:
    """Process metrics on inventory file."""

    __fruitdata: Mapping[str, Sequence[FruitAttributes]] = field(
        default_factory=dict, init=False, repr=False,
    )
    csvfile: Union[Path, PathLike]

    def __post_init__(self):
        self.csvfile = Path(self.csvfile)
        self._load()

    @property
    def inventory(self):
        """Return raw inventory data."""
        return self.__fruitdata

    @property
    def total_fruits(self) -> int:
        """Returns total number of fruits."""
        return len(list(chain.from_iterable(self.__fruitdata.values())))

    @property
    def totals_byfruit(self) -> Mapping[str, int]:
        """Returns totals by fruit in decending order by quanity."""
        return {
            fname: len(attribs)
            for fname, attribs in sorted(
                self.__fruitdata.items(), reverse=True, key=lambda fdata: len(fdata[1])
            )
        }

    @property
    def oldestfruits(self) -> Tuple[Sequence[str], int]:
        """Returns oldest fruit(s) and age."""
        data = defaultdict(set)
        for fname, fatrs in self.__fruitdata.items():
            for fatr in fatrs:
                data[fatr.age].add(fname)
        age = sorted(data, reverse=True)[0]
        return data[age], age

    @property
    def total_fruittypes(self) -> int:
        """Returns total number of fruits by type."""
        return len(self.__fruitdata.keys())

    @property
    def totals_bychar(self) -> Mapping[Counter[int], str]:
        """Returns total number of fruits by characteristics ."""
        return {
            fname: dict(Counter([fatr.char for fatr in fatrs]))
            for fname, fatrs in self.__fruitdata.items()
        }

    def _load(self) -> None:
        """Reads CSV data."""
        logging.debug(self.csvfile)
        self.__fruitdata = defaultdict(list)
        with self.csvfile.open() as fid:
            reader = csv.reader(fid, skipinitialspace=True, strict=True)
            total_fields = len(next(reader))
            for line in reader:
                if len(line) != total_fields or not line[1].isnumeric():
                    raise DataError(self.csvfile)
                self.__fruitdata[line[0]].append(FruitAttributes(int(line[1]), tuple(line[2:])))


def report(basket: FruitBasket) -> str:
    """Return report data.

    Args:
        basket (FruitBasket): Inventory data to generate report.

    Returns:
        str: Report document.
    """
    report_lines = deque()
    report_lines.append(f"Total number of fruit:\n{basket.total_fruits}")
    report_lines.append(f"Total types of fruit:\n{basket.total_fruittypes}")
    fruits, age = basket.oldestfruits
    report_lines.append(
        "Oldest fruit & age:\n{}".format("\n".join(f"{fname}: {age}" for fname in fruits))
    )
    report_lines.append(
        "The number of each type 1of fruit in descending order:\n{}".format(
            "\n".join(f"{fname}: {count}" for fname, count in basket.totals_byfruit.items())
        )
    )
    report_lines.append(
        "The various characteristics (count, color, shape, etc.) of each fruit by type:\n{}".format(
            "\n".join(
                f"{count} {fname}: {' '.join(fatr)}"
                for fname, fatrs in basket.totals_bychar.items()
                for fatr, count in fatrs.items()
            )
        )
    )

    return "\n\n".join(report_lines)
