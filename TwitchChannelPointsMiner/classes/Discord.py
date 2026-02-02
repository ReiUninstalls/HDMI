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
                    "username": "Seol Hee",
                    "avatar_url": "https://media.discordapp.net/attachments/1465033491392761990/1467619998544564428/13.jpg?ex=69810b22&is=697fb9a2&hm=85a864102e1d2a2d0501cd1c0695e44afe8189ee478095c8a60d2af8aac301a2&=&format=webp&width=1768&height=673",
                },
            )
