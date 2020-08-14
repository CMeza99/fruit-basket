"""Main definitions of classes and functions."""
import csv
import logging
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from itertools import chain
from pathlib import Path
from typing import Mapping, Sequence, Tuple


# Note: Setting compare and hash to false does not prevent attribute from being included in the hash.
@dataclass(eq=True, frozen=True)
class FruitAttributes:
    """Atributes of fruit."""

    # Char should probably be a set, but the desired report show characteristics order matter.
    age: field(default=int, compare=False, hash=False)
    char: Tuple[str]


def readfiledata(csvfile: Path) -> Mapping[str, Sequence[FruitAttributes]]:
    """Read and parse CSV file.

    Args:
        csvfile (Path): Path to CSV file.

    Raises:
        execption: [description]
        Exception: [description]

    Returns:
        Mapping[str, Sequence[FruitAttributes]]: Data from CSV file.
    """
    logging.debug(csvfile)
    rtn = defaultdict(list)
    with csvfile.open() as fid:
        reader = csv.reader(fid, skipinitialspace=True, strict=True)
        total_fields = len(next(reader))
        for line in reader:
            if not line:
                continue
            # if len(line) != total_fields or not line[1].isnumeric():
            #     # TODO: raise execption for invalid csv
            #     raise Exception
            rtn[line[0]].append(FruitAttributes(int(line[1]), tuple(line[2:])))
        return rtn


def sumallfruit(fruitdata: Mapping[str, Sequence[FruitAttributes]]) -> int:
    """Calculate total number of fruits.

    Args:
        fruitdata (Mapping[str, Sequence[FruitAttributes]]): Fruit info

    Returns:
        int: Total number fruits.
    """
    return len(list(chain.from_iterable(fruitdata.values())))


def sumeachfruit(fruitdata: Mapping[str, Sequence[FruitAttributes]]) -> Mapping[str, int]:
    return {name: len(attribs) for name, attribs in fruitdata.items()}


def oldestfruit(fruitdata: Mapping[str, Sequence[FruitAttributes]]) -> Sequence[str]:
    """Get name(s) of the oldest fruit.

    Args:
        fruitdata (Mapping[str, Sequence[FruitAttributes]]): Fruit info

    Returns:
        Sequence[str]: The oldest fruit(s).

    """
    data = defaultdict(set)
    for fruitname, attribs in fruitdata.items():
        for attrib in attribs:
            data[attrib.age].add(fruitname)
    age = sorted(data, reverse=True)[0]
    return data[age], age


def totaltypes(fruitdata: Mapping[str, Sequence[FruitAttributes]]) -> int:
    return len(fruitdata)


def countbychar(fruitdata: Mapping[str, Sequence[FruitAttributes]]):
    return {
        name: Counter([attrib.char for attrib in attribs]) for name, attribs in fruitdata.items()
    }
