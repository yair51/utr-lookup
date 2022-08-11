import requests
import os
from os.path import exists as file_exists
from dotenv import load_dotenv
import pickle
load_dotenv()


def utr_login():
    """Log in to UTR"""

    # Contact API
    data = {"email": os.getenv("UTR_EMAIL"),
            "password": os.getenv("UTR_PASSWORD")}
    s = requests.Session()
    r = s.post('https://app.universaltennis.com/api/v1/auth/login', json=data)

    # Store cookies in external file
    with open('cookies.pickle', 'wb') as f:
        pickle.dump(s.cookies, f)


def utr_search(name):
    """Search UTR of given player"""

    # If 'cookies.pickle' file doesn't exist, authenticate with UTR
    if not file_exists('cookies.pickle'):
        utr_login()

    # Fetch cookies from external file
    with open('cookies.pickle', 'rb') as f:
        cookies = pickle.load(f)

    # Contact API
    query = {"query": name, "top": 10}
    try:
        r = requests.get(
            'https://api.universaltennis.com/v2/search/players', data=query, cookies=cookies)
        r.raise_for_status()
    except requests.RequestException as err:
        print(err)
        return None

    # Parse response
    try:
        players = []
        utr = r.json()
        for count, player in enumerate(utr["hits"]):
            players.append({
                "name": player["source"]["displayName"],
                "singlesUtr": player["source"]["singlesUtrDisplay"],
                "singlesRatingAccuracy": int(player["source"]["ratingProgressSingles"]),
                "doublesUtr": player["source"]["doublesUtrDisplay"],
                "doublesRatingAccuracy": int(player["source"]["ratingProgressDoubles"]),
                "threeMonthRating": player["source"]["threeMonthRatingChangeDetails"]["ratingDisplay"]
            })
        return players
    except (KeyError, TypeError, ValueError):
        return None


def is_authenticated(players):
    """Check if already authenticated with UTR. Returns True if logged in."""

    # Check JSON response for login status
    for player in players:
        if ("x" in player["singlesUtr"] or "x" in player["doublesUtr"]):
            return False
    return True
