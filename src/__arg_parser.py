import argparse


def parse_args():
    """
    Parses debug and folder arguments.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False
    csv (str): Path to CSV file containing users to create.

    Returns: (argparse.Namespace): Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        required=False,
        help="Enable debug logging",
    )
    parser.add_argument(
        "--csv",
        type=str,
        required=True,
        help="Path to CSV file containing users to create.",
    )
    return parser.parse_args()
