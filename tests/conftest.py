"""Configuration for tests."""
import fruit_basket


def pytest_report_header():
    """Additional report header."""
    return f"version: {fruit_basket.__version__}"
