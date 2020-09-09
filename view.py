# -*- coding: utf-8 -*-
from flask import request, send_file
from app import app
from errors import ApiErrors
from bot_data import message_new

import json


exc = ApiErrors()


@app.route('/', methods=["GET"])
def index():
    return {'status': 'ok'}


@app.route('/morgen', methods=['GET'])
def morgen():
    return send_file('res/morgen.mp4', attachment_filename='morgen.mp4')


@app.route('/vk', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    else:

        if ('secret' in data) and data['secret'] == app.config['VK_SECRET']:

            if data['type'] == 'confirmation':
                return app.config['VK_CONFIRMATION']
            elif data['type'] == 'message_new':
                # print(data)
                message_new(data)
                return 'ok'

            else:
                return 'ok'
        else:
            return 'ok'
