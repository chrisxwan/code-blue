from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for, flash)
from flask.ext.login import login_user, logout_user, current_user, login_required
from splash import *
from main import app, db

splash = Blueprint('splash', __name__, template_folder="templates")


@splash.route('/')
def index():
	return "Under Construction"
    # return render_template('home.html')