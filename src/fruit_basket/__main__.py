"""Module interface for Fruit Basket."""
import logging
import sys

from fruit_basket.cli import main as cli


def main():
    """Entrypoint to aoad as Python module."""
    module_args = sys.argv[1:]
    logging.debug("Module arguments received: %s", module_args)
    cli()


if __name__ == "__main__":
    main()
