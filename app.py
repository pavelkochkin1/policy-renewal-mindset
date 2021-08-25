import os
from flask.helpers import url_for

import pandas as pd
from flask import Flask
from flask import request
from flask import render_template, send_file, redirect, flash

from model.utils import DataPreprocessing
from model.model import Predictor
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/data_test/'

app = Flask(__name__)

@app.route("/data_test", methods=['GET', 'POST'])
def upload_image():
    return render_template("templates/index.html")


if __name__=='__main__':
    predictor = Predictor('model/model_pipeline.joblib')
    app.run(port=8080, debug=True, host='127.0.0.1')
