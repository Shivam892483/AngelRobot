import threading

from sqlalchemy import Column, String

from AngelRobot.modules.sql import BASE, SESSION


class AngelChats(BASE):
    __tablename__ = "Angel_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


AngelChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Angel(chat_id):
    try:
        chat = SESSION.query(AngelChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Angel(chat_id):
    with INSERTION_LOCK:
        Angelchat = SESSION.query(AngelChats).get(str(chat_id))
        if not Angelchat:
            Angelchat = AngelChats(str(chat_id))
        SESSION.add(Angelchat)
        SESSION.commit()


def rem_Angel(chat_id):
    with INSERTION_LOCK:
        Angelchat = SESSION.query(AngelChats).get(str(chat_id))
        if Angelchat:
            SESSION.delete(Angelchat)
        SESSION.commit()
