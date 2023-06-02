from core.base import Event, IncomingMessage
from core import Pythogram


lasagnas = [
    dict(lasagna="sad lasagna", href="https://s3.amazonaws.com/intanibase/iad_screenshots/1982/19945/23.jpg"),
    dict(lasagna="satisfied lasagna", href="https://avante.biz/wp-content/uploads/Garfield-Wallpaper/Garfield-Wallpaper-029.jpg"),
    dict(lasagna="chill lasagna", href="https://i.ibb.co/GkPN6wN/sh.png"),
    dict(lasagna="pensive lasagna", href="https://i.ytimg.com/vi/NNCHcLI-cN8/maxresdefault.jpg"),
    dict(lasagna="bitch lasagna", href="https://uchastniki.com/wp-content/uploads/2019/06/pewdiepie-5.jpg"),
]


class Actionlas(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ["sad lasagna", "satisfied lasagna", "chill lasagna", "pensive lasagna", "bitch lasagna"]

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = message.text
        for lasagna in lasagnas:
            if text == lasagna.get("lasagna"):
                self.__sender.photo.send(
                    file=lasagna.get("href"),
                    chat=message.chat
                )
