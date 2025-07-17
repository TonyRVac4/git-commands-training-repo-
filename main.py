from abc import ABC, abstractmethod


class ABSRepository(ABC):

    @abstractmethod
    def update_bulk(self, data: dict) -> dict:
        ...

    @abstractmethod
    def get(self, id):
        ...
