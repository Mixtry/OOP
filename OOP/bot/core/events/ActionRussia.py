from core.base import Event, IncomingMessage
from core import Pythogram


class ActionRussia(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['привет', 'хай']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = f'Привет, напиши какая ты лазанья(sad lasagna, satisfied lasagna, chill lasagna, pensive lasagna, bitch lasagna)'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
        self.__sender.photo.send(
            file='https://rukami-sam.ru/wp-content/uploads/4/6/2/462ae7a16b938d57517015bdbc7fba76.jpeg',
            chat=message.chat
        )
