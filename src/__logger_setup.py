import sys

try:
    from loguru import logger
except ImportError:
    print("Please pip install loguru")
    sys.exit(1)


def setup_logging(debug: bool):
    """
    Setup loguru logging.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False

    Returns:
    logger (loguru.logger): Loguru logger object.
    """
    # Remove all built in handlers
    logger.remove()
    # Set custom loguru format
    fmt = (
        "<level>{time:YYYY-MM-DD hh:mm:ss A}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{"
        "function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> "
    )
    # Set Debug level if --debug is passed
    if debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")
    else:
        logger.add(sys.stderr, format=fmt, level="INFO")
    return logger


if __name__ == "__main__":
    pass
