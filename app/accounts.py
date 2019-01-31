import os
import json
import datetime
from app import app, #db, login, mail
from flask import Blueprint, render_template, abort, redirect, request, url_for, jsonify
from jinja2 import TemplateNotFound
from config import Config
# from flask_login import login_user, current_user, logout_user, login_required

accounts = Blueprint('accounts', __name__)

@accounts.route('/')
def home():
    return "1"

