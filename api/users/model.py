from api.database.engine import Base
from sqlalchemy import Index, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.likes.model import likes_secondary

from geoalchemy2.types import Geometry, WKBElement

class UserModel(Base):
    __tablename__ = "users"

    name: Mapped[str] 
    description: Mapped[str] 
    age: Mapped[int]
    gender: Mapped[str]
    geo: Mapped[WKBElement] = mapped_column(
        Geometry("POINT", srid=4326)
    )

    likes: Mapped["LikesModel"] = relationship(
        secondary=likes_secondary,
        uselist=True,
    )

    __table_args__ = (
        Index("user_id_idx", "id"),
    )