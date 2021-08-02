# IMPORT STATEMENTS
from flask import Flask, render_template, request, session
import pandas as pd
# import numpy as np
import jinja2
# import requests
# import re

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return render_template('email.html')
    
    #Email Route
    @app.route('/email')
    def email():
        first_name=request.args.get('fname')
        return render_template('email.html', first_name=first_name)
    
    






    return app

