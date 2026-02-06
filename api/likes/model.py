from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, MetaData, Integer

from api.database.engine import Base

class LikesModel(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)

likes_secondary = Table(
    "likes_secondary",
    MetaData(),
    Column("user_id", Integer(), primary_key=True),
    Column("like_id", Integer(), primary_key=True)
)