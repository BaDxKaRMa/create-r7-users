from loguru import logger
import sys
import os

try:
    from dotenv import load_dotenv
except ImportError:
    logger.error("Please pip install python-dotenv")
    sys.exit(1)


def load_env():
    """
    Load environment variables from .env file.

    Returns:
    USERNAME (str): Username to login to R7.
    PASSWORD (str): Password to login to R7.
    BASE_URL (str): Base URL for R7.
    """
    # Load .env file from parent folder
    target_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = os.path.join(target_dir, ".env")
    logger.debug(f"Loading .env file from {dotenv_path}")
    load_dotenv(dotenv_path)

    # Load environment variables
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    BASE_URL = os.getenv("BASE_URL")
    logger.debug("Loaded environment variables")
    logger.debug(f"Username: {USERNAME} | Password: {PASSWORD} | Base URL: {BASE_URL}")
    return USERNAME, PASSWORD, BASE_URL
