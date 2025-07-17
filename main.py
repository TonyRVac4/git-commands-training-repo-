from abc import ABC, abstractmethod


class ABSRepository(ABC):

    @abstractmethod
    def update(self, data: dict) -> dict:
        ...

    @abstractmethod
    def delete(self, id):
        ...
