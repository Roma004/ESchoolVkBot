# -*- coding: utf-8 -*-
from vk_api import vk_api
from app import app
from db import User
import time
from .texts import Texts

vk_session = vk_api.VkApi(token=app.config['VK_TOKEN'])
vk = vk_session.get_api()


def send_msg(peer_id, text, keyboard):
    vk.messages.send(
        peer_id=peer_id,
        message=text,
        keyboard=keyboard,
    )


def message_new(data: dict):
    text = data["object"]["message"]["text"]
    peer_id = data['object']['message']['peer_id']

    user = User.select().where(
        User.user_id == peer_id
    )

    if not user.exists():
        User(
            user_id=peer_id,
            position="main",
            ts=time.time()
        )

        send_msg(
            peer_id=peer_id,
            text=Texts.main_menue
        )

        return

    user = user.get()

    if user.position == "main":
        if text in []:
            ...
