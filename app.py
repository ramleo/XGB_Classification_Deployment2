import werkzeug
import numpy as np
import pandas as pd
from joblib import load
from flask import Flask, request, jsonify, render_template

# Creating app object

app = Flask(__name__)

# Predicting Test data
# Checking the model with single data point from test dataset
# Loading required models

# Loading the saved model
full_model_pipeline = load('udf_full_pipeline')

# Using the html template
@app.route('/')
def home():
    return render_template('index.html')

# Exposing the below code to localhost:5000
@app.route('/api', methods=['POST'])
def pred_testquery():

    # content = request.json
    arpu_diff = float(request.form['arpu_diff'])
    total_rech_amt_diff = float(request.form['total_rech_amt_diff'])
    last_day_rch_amt_8 = float(request.form['last_day_rch_amt_8'])
    total_og_mou_diff = float(request.form['total_og_mou_diff'])
    loc_ic_mou_8 = float(request.form['loc_ic_mou_8'])
    loc_ic_t2m_mou_8 = float(request.form['loc_ic_t2m_mou_8'])
    loc_og_mou_8 = float(request.form['loc_og_mou_8'])
    total_ic_mou_diff = float(request.form['total_ic_mou_diff'])
    loc_og_t2f_mou_8 = float(request.form['loc_og_t2f_mou_8'])
    loc_ic_t2f_mou_8 = float(request.form['loc_ic_t2f_mou_8'])

    datapoint = [arpu_diff, total_rech_amt_diff, last_day_rch_amt_8, total_og_mou_diff, loc_ic_mou_8,
                  loc_ic_t2m_mou_8, loc_og_mou_8, total_ic_mou_diff, loc_og_t2f_mou_8, loc_ic_t2f_mou_8]

    def y_pred(X_data=datapoint, model=full_model_pipeline):

        # Creating a dataframe out of input
        df = pd.DataFrame(index=[0])
        df['arpu_diff'] = X_data[0]
        df['total_rech_amt_diff'] = X_data[1]
        df['last_day_rch_amt_8'] = X_data[2]
        df['total_og_mou_diff'] = X_data[3]
        df['loc_ic_mou_8'] = X_data[4]
        df['loc_ic_t2m_mou_8'] = X_data[5]
        df['loc_og_mou_8'] = X_data[6]
        df['total_ic_mou_diff'] = X_data[7]
        df['loc_og_t2f_mou_8'] = X_data[8]
        df['loc_ic_t2f_mou_8'] = X_data[9]

        # Fitting classifier model
        pred = model.named_steps.Fitting_xgb_model.predict(df)

        return pred

    prediction = y_pred()
    if prediction == 0:
        Churn = "Yes"
    else:
        Churn = "No"
    response = {'Will the customer churn?': Churn}

    return str(response)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)