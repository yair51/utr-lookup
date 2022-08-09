

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("index.html", title="Home")


@views.route('/result')
def result():
    return render_template("result.html", title="Result")