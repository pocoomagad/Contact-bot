from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, MetaData, Integer

from api.database.core import Base

class LikesModel(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)

print(LikesModel().__table__.collumns)

likes_secondary = Table(
    "likes_secondary",
    MetaData(),
    Column("user_id", Integer(), primary_key=True),
    Column("like_id", Integer(), primary_key=True)
)