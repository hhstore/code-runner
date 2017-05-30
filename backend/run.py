#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from flask import Flask, request, jsonify
from flask_restful import Api

from backend.core.apis.runner import Runner

app = Flask(__name__)
api = Api(app)

# restful API:

api.add_resource(Runner, '/run')


@app.route("/")
def index():
    current_time = time.strftime("Current time:\n%Z # %Y-%m-%d # %p %I:%M:%S",
                                 time.localtime(time.time()))

    return "<h1/>Hello, visitor.\r\n %s</h1>" % current_time


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
