from abc import ABC, abstractmethod
from typing import Any, Optional

from telebot import TeleBot
from telebot.types import Message

from repositories import Repo
from config import Config


class Command(ABC):
    def __init__(self,
                 chat: Optional[TeleBot],
                 message: Optional[Message],
                 repo: Optional[Repo]):
        self._chat = chat
        self._message = message
        self._repo = repo

    @abstractmethod
    def exec(self) -> Any:
        pass


class StartCommand(Command):
    def exec(self) -> None:
        self._chat.reply_to(self._message, Config().start_message)


class HelpCommand(Command):
    def exec(self) -> None:
        self._chat.reply_to(self._message, Config().help_message)


class BookmarkCommand(Command):
    def exec(self) -> None:
        self._chat.reply_to(self._message, f"Bookmark:{self._message.text} Saved !")
