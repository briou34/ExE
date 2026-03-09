# /// script
# dependencies = [
#   "requests",
#   "rich",
#   "fake-useragent",
# ]
# ///

import argparse
import logging
import time

import requests
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from rich.console import Console
from urllib3.util import Retry

console = Console()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_smart_session():
    session = requests.Session()

    # Define retry strategy
    # 429 = Too Many Requests, 500/502/503/504 = Server Errors
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False,  # Allow us to handle 429 custom logic manually if needed
    )

    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Set a stable User-Agent for this session
    ua = UserAgent(platforms="desktop")
    session.headers.update({"User-Agent": ua.random})

    return session


SESSION = create_smart_session()


def get_player_info(player_id):
    url = "https://kingshot.net/api/player-info"
    params = {"playerId": str(player_id)}

    try:
        response = SESSION.get(url, params=params, timeout=10)

        # Specific handling for the custom retry-after JSON logic
        if response.status_code == 429:
            try:
                wait = response.json().get("meta", {}).get("details", {}).get("retryAfter", 10)
                logger.warning(f"Rate limited. Manual wait: {wait}s")
                time.sleep(wait)
                # Retry one more time manually if the adapter didn't catch the specific JSON wait
                response = SESSION.get(url, params=params, timeout=10)
            except (ValueError, KeyError):
                pass

        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    return None


def main():
    parser = argparse.ArgumentParser(description="Fetch player info.")
    parser.add_argument("player_id", type=int, help="ID of the player")
    args = parser.parse_args()

    player_info = get_player_info(args.player_id)
    if player_info and "data" in player_info:
        for key, value in player_info["data"].items():
            console.print(f"[bold]{key}:[/bold] {value}")
    else:
        console.print("[red]Failed to retrieve player info.[/red]")


if __name__ == "__main__":
    main()
