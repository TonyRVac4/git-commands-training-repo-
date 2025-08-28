from abc import ABC, abstractmethod

class ABSRepository(ABC):

    @abstractmethod
    def update_self(self, data: dict) -> dict:
        ...

    @abstractmethod
    def list_items(self, id) -> list:
        ...

    @abstractmethod
    def delete(self, id):
        ...
print("hello world")