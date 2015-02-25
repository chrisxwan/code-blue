from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for, flash)
from flask.ext.login import login_user, logout_user, current_user, login_required
from splash import *
from main import app, db

splash = Blueprint('splash', __name__, template_folder="templates")


@splash.route('/')
def index():
    return render_template('home.html')

@splash.route('/mentors', methods=['GET', 'POST'])
def mentors():
  if request.method == 'GET':
      return render_template('mentors.html')

  # POST to Google
  print request.form
  return redirect(url_for('splash.index'))

@splash.route('/students', methods=['GET', 'POST'])
def students():
  if request.method == 'GET':
      return render_template('students.html')

  # POST to Google
  print request.form
  return redirect(url_for('splash.index'))