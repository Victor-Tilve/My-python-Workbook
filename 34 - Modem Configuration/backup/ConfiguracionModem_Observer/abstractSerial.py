from __future__ import annotations
from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
from abstractModem import AbstractModem

class AbstractSerial(ABC):
    """
    The AbstractModem interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, abstractModem: AbstractModem) -> None:
        """
        Attach an AbstractModem to the AbstractSerial.
        """
        pass

    @abstractmethod
    def detach(self, abstractModem: AbstractModem) -> None:
        """
        Detach an abstractModem from the AbstractSerial.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all AbstractModems about an event.
        """
        pass
