import requests
import os
from dotenv import load_dotenv
import pickle
load_dotenv()

def utr_login():
    """Log in to UTR"""

    # Contact API
    data = {"email": os.getenv("UTR_EMAIL"), "password": os.getenv("UTR_PASSWORD")}
    s = requests.Session()
    r = s.post('https://app.universaltennis.com/api/v1/auth/login',json=data)

    # Store cookies in external file
    with open('cookies.pickle', 'wb') as f:
        pickle.dump(s.cookies, f)
        print("done")


def utr_search(name):
    """Search UTR of given player"""

    # Fetch cookies from external file
    with open('cookies.pickle', 'rb') as f:
        cookies = pickle.load(f)

    # Contact API
    query = {"query": name}
    try:
        r = requests.get('https://api.universaltennis.com/v2/search/players', data=query, cookies=cookies)
        r.raise_for_status()
    except requests.RequestException as err:
        print(err)
        return None

    # Parse response

    utr = r.json()
    for i in range(10):
        print(utr["hits"][i]["source"]["singlesUtr"])

utr_login()
