from typing import TYPE_CHECKING

from core.models.base import Base
from core.models.mixins.id_int_pk import IdIntPkMixin
from core.types.user_id import UserIdType
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
