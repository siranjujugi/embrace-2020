#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pickle
from flask import Flask, jsonify, request
from schema import Schema, And, Or, SchemaError

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

PREDICT_SCHEMA = Schema({
    'CHARGE_COUNT': int,
    'CHARGE_DISPOSITION': And(str, len),
    'OFFENSE_CATEGORY': And(str, len),
    'PRIMARY_CHARGE_FLAG': bool,
    'DISPOSITION_CHARGED_OFFENSE_TITLE': And(str, len),
    'DISPOSITION_CHARGED_CLASS': And(str, len),
    'SENTENCE_JUDGE': And(str, len),
    'SENTENCE_PHASE': And(str, len),
    'COMMITMENT_TERM': And(str, len),
    'COMMITMENT_UNIT': And(str, len),
    'LENGTH_OF_CASE_in_Days': Or(float, int),
    'AGE_AT_INCIDENT': Or(float, int),
    'RACE': And(str, len),
    'GENDER': And(str, len),
    'INCIDENT_CITY': And(str, len),
    'LAW_ENFORCEMENT_AGENCY': And(str, len),
    'LAW_ENFORCEMENT_UNIT': And(str, len),
    'SENTENCE_TYPE': And(str, len)
}, ignore_extra_keys=True)

PREDICT_KEYS = [
    'CHARGE_COUNT',
    'CHARGE_DISPOSITION',
    'OFFENSE_CATEGORY',
    'PRIMARY_CHARGE_FLAG',
    'DISPOSITION_CHARGED_OFFENSE_TITLE',
    'DISPOSITION_CHARGED_CLASS',
    'SENTENCE_JUDGE',
    'SENTENCE_PHASE',
    'COMMITMENT_TERM',
    'COMMITMENT_UNIT',
    'LENGTH_OF_CASE_in_Days',
    'AGE_AT_INCIDENT',
    'RACE',
    'GENDER',
    'INCIDENT_CITY',
    'LAW_ENFORCEMENT_AGENCY',
    'LAW_ENFORCEMENT_UNIT',
    'SENTENCE_TYPE',
]


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = PREDICT_SCHEMA.validate(request.json)
    except SchemaError as error:
        return jsonify(message=str(error)), 404

    # Ensure these are floats, not ints for the model
    data['LENGTH_OF_CASE_in_Days'] = float(data['LENGTH_OF_CASE_in_Days'])
    data['AGE_AT_INCIDENT'] = float(data['AGE_AT_INCIDENT'])

    # Convert JSON to array to pass to the model
    data = [data[k] for k in PREDICT_KEYS]

    # TEMP to convert to the example model until we get the real one
    data = [float(data[0])]

    probability = model.predict([data])

    return {
        'bias_probability': probability[0],
    }
