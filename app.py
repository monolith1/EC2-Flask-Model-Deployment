import flask
import pickle

# import packages used by model

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_regression

# define functions used by model

def to_dense(x):
    return x.toarray()
to_dense_transformer = FunctionTransformer(to_dense)

def credit_nan(x):
    return x.replace(np.nan, 0)
credit_nan_transformer = FunctionTransformer(credit_nan)

# Use pickle to load in the pre-trained model.

with open(f'model/clf.p', 'rb') as f:
    model = pickle.load(f)

# instantiate app

app = flask.Flask(__name__, template_folder='templates')

# app routing

@app.route('/', methods=['GET', 'POST'])


def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        gender = flask.request.form['gender']
        married = flask.request.form['married']
        dependents = flask.request.form['dependents']
        education = flask.request.form['education']
        self_employed = flask.request.form['self_employed']
        income = flask.request.form['income']
        coincome = flask.request.form['coincome']
        amount = flask.request.form['amount']
        term = flask.request.form['term']
        history = flask.request.form['history']
        area = flask.request.form['area']
        input_variables = pd.DataFrame([[gender, married, dependents, education, self_employed, income, coincome, amount, term, history, area]],
                                       columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                                               'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                                               'Loan_Amount_Term', 'Credit_History', 'Property_Area'])
        if model.predict(input_variables)[0] == 1:
            return flask.render_template('main.html',
                                         original_input={'Gender': gender,
                                                         'Married': married,
                                                         'Dependents': dependents,
                                                         'Education': education,
                                                         'Self_Employed' : self_employed,
                                                         'ApplicantIncome': income,
                                                         'CoapplicantIncome': coincome,
                                                         'LoanAmount': amount,
                                                         'Loan_Amount_Term': term,
                                                         'Credit_History': history,
                                                         'Property_Area' : area},
                                         result='Approved',
                                         )
        elif model.predict(input_variables)[0] == 0:
            return flask.render_template('main.html',
                                         original_input={'Gender': gender,
                                                         'Married': married,
                                                         'Dependents': dependents,
                                                         'Education': education,
                                                         'Self_Employed' : self_employed,
                                                         'ApplicantIncome': income,
                                                         'CoapplicantIncome': coincome,
                                                         'LoanAmount': amount,
                                                         'Loan_Amount_Term': term,
                                                         'Credit_History': history,
                                                         'Property_Area' : area},
                                         result='Denied',
                                         )

# Run the app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)