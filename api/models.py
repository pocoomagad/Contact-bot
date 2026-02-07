from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def to_dict(self) -> dict:
        return self.c

    def __repr__(self):
        return f"{self.__class__.__name__}"