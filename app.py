# -*- coding: utf-8 -*-
from flask import Flask
from config.config import Config
from errors import ApiErrors

exc = ApiErrors()
app = Flask(__name__)
app.config.from_object(Config)


@app.errorhandler(500)
def handler_500(error):
    print(error)
    return exc.return_error(500), 500


@app.errorhandler(404)
def handler_404(error):
    return exc.return_error(404), 404


@app.errorhandler(405)
def handler_405(error):
    return exc.return_error(405), 405
