from abc import ABC, abstractmethod

from sqlalchemy import select, insert, update
from api.users.models import UserModel
from api.abc import BaseRepository

class AbstractUserRepository(ABC):
    @abstractmethod
    async def select_user_by_id(self, id: int):
        ...

    @abstractmethod
    async def select_users(self):
        ...

    @abstractmethod
    async def insert_user(self, id: int, data: dict):
        ...

    @abstractmethod
    async def update_user(self, id: int, data: dict):
        ...

class UserRepository(AbstractUserRepository, BaseRepository):
    async def select_user_by_id(self, id: int) -> UserModel:
        result = self.session.execute(
            select(UserModel)
            .filter_by(id=id)
        )
        await session.commit()
        return result.scalars().all()
        
    async def select_users(self):
        result = (
            self.session.execute(
                select(UserModel)
            )
        )
        await session.commit()
        return result.scalars().all()

    async def insert_user(self, id: int, data: dict) -> int:
        result = (
            self.session.execute(
                insert(UserModel)
                .filter_by(id=id)
                .values(**data)
                .returning(UserModel.id)
            )
        )
        await session.commit()
        return result.scalar()

    async def update_user(self, id: int, data: dict) -> int:
        result = (
            self.session.execute(
                update(UserModel)
                .filter_by(id=id)
                .values(**data)
                .returning(UserModel.id)
            )
        )    
        await session.commit()
        return result.scalar()