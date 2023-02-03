from abc import ABC, abstractmethod
from typing import List


class Parser(ABC):
    def __init__(self, src: str):
        self.__src = src

    @property
    @abstractmethod
    def description(self) -> str | None:
        """Returns description, if it does not exist, raises exception"""
        pass

    @property
    @abstractmethod
    def images(self) -> List[str] | None:
        """Returns url list, if they do not exist, raises exception"""
        pass

    @property
    @abstractmethod
    def title(self) -> str | None:
        """Returns page title, if it does not exist, raises exception"""
        pass

    @property
    @abstractmethod
    def icon(self) -> str | None:
        """Returns url, if it does not exist, raises exception"""
        pass
