import os
import csv
import json
import datetime
from flask import render_template, flash, redirect, request, url_for, jsonify
from app import app, db, login
from config import Config
from app.forms import 
from app.models import
from flask_login import login_user, current_user, logout_user, login_required

@login.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@login.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))