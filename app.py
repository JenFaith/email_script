import pandas
import numpy
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    
    #Testing route
    @app.route('/')
    def home():
        return render_template('email.html')

    return app

