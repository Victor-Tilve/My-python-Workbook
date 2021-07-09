from __future__ import annotations
from abc import ABC, abstractmethod #https://docs.python.org/3/library/abc.html
from abstractSerial import AbstractSerial

class AbstractModem(ABC):
    """
    The AbstractModem interface declares the update method, used by abstractSerial.
    """

    @abstractmethod
    def update(self, abstractSerial: AbstractSerial) -> None:
        """
        Receive update from abstractSerial.
        """
        pass
