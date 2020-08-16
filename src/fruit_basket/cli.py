"""Fruit Basket CLI."""
import argparse
import sys

from fruit_basket import __version__, FruitBasket, report


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fruit Basket CLI Help", allow_abbrev=False)

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType(), help="Fruit basket inventory file(csv)."
    )

    return parser


def main():
    """Entrypoint for console."""
    parser = _create_parser()

    if len(sys.argv) == 1:
        parser.error("File required")

    args = parser.parse_args()
    args.file.close()
    print(report(FruitBasket(args.file.name)))


if __name__ == "__main__":
    main()
