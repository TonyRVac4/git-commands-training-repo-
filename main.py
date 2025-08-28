from abc import ABC, abstractmethod


class ABSRepository(ABC):

    @abstractmethod
    def update_self(self, data: dict) -> dict:
        ...

    @abstractmethod
    def get_item_by_id(self, id):
        return 12

    @abstractmethod
    def delete(self, id):
        ...
