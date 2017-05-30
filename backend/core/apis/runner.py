#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource, reqparse, abort

from backend.core.services.runner import CodeRunner
from backend.core.settings import ContainerConfig

parser = reqparse.RequestParser()

# 参数校验:
parser.add_argument("lang", type=str)
parser.add_argument("code", type=str)


class Runner(Resource):
    def post(self):
        #data = request.get_json()
        data = parser.parse_args()
        lang = data.get("lang").lower()  # 语言类型不区分大小写
        code = data.get("code")

        # 编程语言类型不支持:
        if lang not in ContainerConfig.language_support:
            abort(400)   # 参数不合法, 直接返回 [400 Bad Request]

        r = CodeRunner(code, lang)
        return r.run()

