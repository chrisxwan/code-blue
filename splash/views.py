from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for, flash)
from flask.ext.login import login_user, logout_user, current_user, login_required
from splash import *
from main import app, db
import requests

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
    url = "https://docs.google.com/forms/d/1hp7fFopNM9wH9JrbjQPonmC-V2Fsk7XKlMCCd4_XESE/formResponse"
    payload = {
      "entry_1936930932" : request.form['name'],
      "entry_1213247573" : request.form['email'],
      "entry_1595147491" : request.form['phone'],
      "entry_369883752"  : request.form['school'],
      "entry_1041567284" : request.form['html'],
      "entry_1999826878" : request.form['css'],
      "entry_915431056"  : request.form['javascript'],
      "entry_440391179"  : request.form['meteor'],
      "entry_122881673"  : request.form['entrepreneurship']
    }
    r = requests.post(url, data=payload)

    return redirect(url_for('splash.index'))

@splash.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        message = ""
        return render_template('students.html', message=message)

    if (request.form['name']=="" or request.form['email']=="" or request.form['year']=="" or request.form['school']=="" or request.form['city']=="" or request.form['emergency_name']=="" or request.form['emergency_number']=="" or request.form['emergency_name']==""):
        message = "Please fill all fields"
        return render_template('students.html', message=message)
    # POST to Google
    url = "https://docs.google.com/forms/d/1G_OpW-8__XR7Chtw-zg8knHSinYr_9uGPAlzQLBBo3Q/formResponse"
    payload = {
      "entry_1936930932" : request.form['name'],
      "entry_1213247573" : request.form['email'],
      "entry_1286191822" : request.form['year'],
      "entry_1595147491" : request.form['school'],
      "entry_369883752"  : request.form['city'],
      "entry_286764877"  : request.form['emergency_name'],
      "entry_2012747492" : request.form['emergency_number'],
      "entry_1547565125" : request.form['emergency_email'],
      "entry_929537745"  : request.form['emergency_relationship'],
      "entry_1041567284" : request.form['html'],
      "entry_1999826878" : request.form['css'],
      "entry_915431056"  : request.form['javascript'],
      "entry_440391179"  : request.form['meteor'],
      "entry_122881673"  : request.form['gender']
    }
    r = requests.post(url, data=payload)

    return redirect(url_for('splash.index'))
