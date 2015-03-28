from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, jsonify, g, url_for, flash)
from main import app

live = Blueprint('live', __name__, template_folder="templates")

@live.route('/')
def index():
  return render_template('live.html')