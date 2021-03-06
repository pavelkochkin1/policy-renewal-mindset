import os

import pandas as pd
from flask import Flask
from flask import request
from flask import render_template, Response

from model.utils import DataPreprocessing
from model.model import Predictor


UPLOAD_FOLDER = 'data/'

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=["GET", "POST"])
def upload_predict():

    if request.method == "POST":
        data_file = request.files["file"]
        file_location = os.path.join(
            UPLOAD_FOLDER,
            data_file.filename
        )

        if data_file:

            data_file.save(file_location)
            data = pd.read_csv(file_location, index_col='POLICY_ID', )
            pred = predictor(data)



            global out_loc, filename
            filename = data_file.filename[:-4]
            out_loc = os.path.join(
                UPLOAD_FOLDER,
                filename+"_output.csv",
            )

            pred.to_csv(out_loc)

            return render_template(
                "download.html",
                out_loc=out_loc
            )

    return render_template("predict.html", out_loc=None)

@app.route("/download")
def download():
    outname = filename+"_output.csv"
    with open(out_loc) as fp:
        data = fp.read()
    return Response(
        data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 f"attachment; filename={outname}"})




if __name__=='__main__':
    predictor = Predictor('model/model_pipeline.joblib')
    app.run(port=8080, debug=True, host='0.0.0.0')
