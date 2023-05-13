#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from src.__arg_parser import parse_args

    args = parse_args()
    # Setup logging before importing other modules
    from src.__logger_setup import setup_logging

    logger = setup_logging(args.debug)

    from src.__setup_env import load_env
    from src.__csv_parser import parse_csv
    import src.r7api as r7api
except ImportError as e:
    print(e)
    exit(1)

if __name__ == "__main__":
    # Load environment variables
    USERNAME, PASSWORD, BASE_URL = load_env()

    # Parse CSV file and print users
    users = parse_csv(args.csv)

    # Create API object
    api = r7api.InsightVM(USERNAME, PASSWORD, BASE_URL)

    # Login to InsightVM
    api.login()
