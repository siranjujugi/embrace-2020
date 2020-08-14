#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pickle
from flask import Flask, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    years = request.json['years']
    salary = model.predict([[years]])
    return f"Predicted salary is ${salary[0]}\n"

