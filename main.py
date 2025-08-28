from abc import ABC, abstractmethod

class ABSRepository(ABC):

    @abstractmethod
    def update_self(self, data: dict) -> dict:
        ...

    @abstractmethod
    def get(self, id):
        ...

    @abstractmethod
    def delete(self, id):
        ...
print("hello world")