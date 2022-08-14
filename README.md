# Free UTR Lookup
#### Video Demo:  <URL HERE>

#### Description:
The Universal Tennis Rating (UTR) is a global tennis player rating system that allows players to determine their level relative to others. The scale rangles from approximately 0 to 16.5, where higher ratings are better. To check ratings of non-professional players with 2 decimal places, a power subscription is required, which costs $10/month or $120/year. Many tennis players pay for a subscription, but most do not. My website allows people to find any UTR with decimals for free. My site logs into the UTR through its API and executes searches from my account, returning results to the users of my website. <br/><br/>

To avoid uneccesary requests to the API, I store my cookies in a .pickle file, and then add those cookies to every search. This allows me to avoid logging into Universal Tennis until my session expires. My website code is found in the website folder, and main.py (located outside the folder) runs the website. This allows me to logically separate the execution and development of my website.
__init__.py file creates the Flask app and returns it to main.py.
config.py contains 3 different classes, which contain configuration variables for development, staging, and production. Grouping the configurations into a base class with 2 child classes allows me to have configuration variables already set and only override the variables I wanted to change.
helpers.py contains all of the functions that allow me to interact with the Universal Tennis API and execute queries.
views.py contains all of the routes accessed in the Flask application. I placed this in a separate file from __init__.py because it is easier to understand that the file only contains views.
base.html contains the header, footer, and links in Bootstrap and CSS files. The main tag contains a block, where Jinja2 inserts the other pages.
index.html displays the homepage, which contains basic instructions for how to use the site.
result.html dynamically displays all of the search results from the API call in an Bootstrap table.

## Setup & Installtion

Make sure you have the latest version of Python installed. It is recommended to use a virtual enviornment.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```
create .env file in root directory with:
```
UTR_EMAIL = {utr_email_here}
UTR_PASSWORD = {utr_password_here}
SECRET_KEY = {secret_key_here}
```

## Running The App

```bash
export FLASK_APP=main.py
flask run
```

## Viewing The App

Go to `http://127.0.0.1:5000`