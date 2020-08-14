#!/usr/bin/env python3
# -*- coding: utf8 -*-

from flask import Flask


app = Flask(__name__)


@app.route('/')
def root():
    return "Hello world!"
