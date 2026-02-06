from fastapi import Request
from sqlalchemy import Select
from api.database.engine import Session

class BaseRepository:
    def __init__(self, session: Session, request: Request):
        self.session = session
        self.request = request

    def pagination(self, query: Select):
        ...