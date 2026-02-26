from textwrap import dedent

import requests

from TwitchChannelPointsMiner.classes.Settings import Events


class Discord(object):
    __slots__ = ["webhook_api", "events"]

    def __init__(self, webhook_api: str, events: list):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]

    def send(self, message: str, event: Events) -> None:
        if str(event) in self.events:
            requests.post(
                url=self.webhook_api,
                data={
                    "content": dedent(message),
                    "username": "Kurumi Underwear",
                    "avatar_url": "https://media.discordapp.net/attachments/1476107573387202642/1476460252085096500/71c02e26982abb2c82503f0f18a56ea59ab85d12122f4595b7ae9b806a6c29b3.png?ex=69a13443&is=699fe2c3&hm=40320fc1853f571b32e7191b600e064786b1d5e0a86dad6d78f73fcb2c10491b&=&format=webp&quality=lossless",
                },
            )
