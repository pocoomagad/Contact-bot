from abc import ABC, abstractmethod
from api.users.repository import AbstractUserRepository

class AbstractUserService(ABC):
    @abstractmethod
    async def get_user():
        ...

    @abstractmethod
    async def get_users():
        ...

    @abstractmethod
    async def create_user():
        ...

    @abstractmethod
    async def update_user():
        ...

class UserService(AbstractUserService):
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo()

    async def get_user(self, id: int):
        ...

    async def get_users(self):
        ...

    async def create_user(self, id: int, data: dict):
        ...

    async def update_user(self, id: int, data: dict):
        ...