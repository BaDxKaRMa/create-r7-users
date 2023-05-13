import csv
import os
import sys
from loguru import logger
from typing import List, Dict


def parse_csv(csv_file) -> List[Dict]:
    """
    Parse CSV file, check headers, and return list of dictionaries
    """
    target_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_filepath = os.path.join(target_dir, csv_file)
    logger.debug(f"CSV file path: {csv_filepath}")
    try:
        with open(csv_filepath, "r") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                logger.error(f"CSV file is empty")
                sys.exit(1)
            acceptable_headers = [
                "username",
                "first_name",
                "last_name",
                "email",
                "role",
                "sites",
                "groups",
            ]
            if not all(header in reader.fieldnames for header in acceptable_headers):
                logger.error(
                    f"CSV file headers are incorrect. Acceptable headers: {acceptable_headers}"
                )
                logger.error(f"CSV file headers: {reader.fieldnames}")
                sys.exit(1)
            list_from_csv = []
            for row in reader:
                list_from_csv.append(row)
            logger.debug(f"CSV file contents: {list_from_csv}")
            return list_from_csv
    except FileNotFoundError:
        logger.error(f"CSV file not found at {csv_filepath}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unknown error: {e}")
        sys.exit(1)
