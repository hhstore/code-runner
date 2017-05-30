#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from backend.core.services.runner import CodeRunner


class Runner(Resource):
    def post(self):
        data = request.get_json()
        lang = data.get("lang")
        code = data.get("code")

        r = CodeRunner(code, lang)
        return r.run()

