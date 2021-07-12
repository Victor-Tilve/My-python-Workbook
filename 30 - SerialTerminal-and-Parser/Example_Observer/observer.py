from __future__ import annotations
from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
# from subject import Subject

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass
