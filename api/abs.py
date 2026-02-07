from fastapi import Request

from abc import ABC

from pydantic import ConfigDict

from typing import ClassVar

from pathlib import Path
import os

from api.database.core import Session

class BaseRepository(ABC):
    def session():
        return Session

class ContactModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        from_attributes=True
    )
    