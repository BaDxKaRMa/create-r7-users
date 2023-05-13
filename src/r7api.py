from dataclasses import dataclass
from typing import Dict, Optional, List
from loguru import logger
import requests


@dataclass
class InsightVMUser:
    id: int
    email: str
    enabled: bool
    login: str
    name: str
    # role: Dict[bool, bool, int, bool]
    authentication_type: str = "SAML"
    links: Optional[List[Dict[str, str]]] = None
    locked: Optional[bool] = None


class InsightVM:
    def __init__(self, username, password, base_url):
        """
        InsightVM API class.
        """
        self.username = username
        self.password = password
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.session.headers.update({"Accept": "application/json"})
        self.session.headers.update({"Content-Type": "application/json"})

    def make_request(self, request_func, *args, **kwargs):
        try:
            response = request_func(*args, **kwargs)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e}")
            raise SystemExit(1)
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection Error: {e}")
            raise SystemExit(1)
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout Error: {e}")
            raise SystemExit(1)
        except requests.exceptions.RequestException as e:
            logger.error(f"General Request Error: {e}")
            raise SystemExit(1)

        return response

    def login(self):
        """
        Login to InsightVM and get a session token.
        """
        url = f"{self.base_url}/api/3/session"
        logger.debug(f"Login URL: {url}")
        response = self.make_request(self.session.post, url, timeout=10)

        try:
            token = response.json()["token"]
        except KeyError:
            logger.error("No token found in the response.")
            raise

        logger.success("Login successful.")
        self.session.headers.update({"Session-Token": token})

    def logout(self):
        """
        Logout of InsightVM and invalidate the session token.
        """
        url = f"{self.base_url}/api/3/session"
        logger.debug(f"Logout URL: {url}")
        response = self.make_request(self.session.delete, url, timeout=10)
        logger.success("Logout successful.")

    def get_users(self):
        """
        Get all users from InsightVM.
        """
        url = f"{self.base_url}/api/3/users"
        logger.debug(f"Get Users URL: {url}")
        response = self.make_request(self.session.get, url, timeout=10)
        return response.json()

    def get_user(self, username):
        """
        Get a single user from InsightVM.
        """
        url = f"{self.base_url}/api/3/users/{username}"
        logger.debug(f"Get User URL: {url}")
        response = self.make_request(self.session.get, url, timeout=10)
        return response.json()
