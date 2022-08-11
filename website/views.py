

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from .helpers import is_authenticated, utr_login, utr_search


views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    """Displays home screen"""
    return render_template("index.html", title="Home")


@views.route('/result')
def result():
    """Displays search results"""
    return render_template("result.html", title="Result")


@views.route('/search')
def search():
    """calls UTR API to search player"""

    # Submit search query to UTR
    query = request.args.get("query")
    results = utr_search(query)

    # Login to UTR and rerun search query if not authenticated
    if not is_authenticated(results):
        utr_login()
        results = utr_search(query)

    return render_template("result.html", results=results)
