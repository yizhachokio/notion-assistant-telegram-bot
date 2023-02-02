from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict
import json


@dataclass
class User:
    id: str
    notion_token: str
    bookmarks_database_id: str


class Repo(ABC):
    @abstractmethod
    def get_user(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass


class JSONRepo(Repo):
    def __init__(self, repo_path: str):
        self._repo_path: str = repo_path
        self._database: Dict[str, Dict[str, str]] = {}

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    def get_user(self, user_id: str) -> User | None:
        return User(user_id,
                    self._database[user_id]['notion_token'],
                    self._database[user_id]['bookmarks_database_id'])

    def update_user(self, user: User) -> None:
        self._database.update({
            user.id: {
                'notion_token': user.notion_token,
                'bookmarks_database_id': user.bookmarks_database_id
            }
        })

    def load(self):
        with open(self._repo_path, 'r') as f:
            self._database = json.load(f)

    def save(self):
        with open(self._repo_path, 'w') as f:
            json.dump(obj=self._database,
                      fp=f,
                      indent=4)
