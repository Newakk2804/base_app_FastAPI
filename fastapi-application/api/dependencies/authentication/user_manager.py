from typing import TYPE_CHECKING, Annotated

from api.dependencies.authentication.users import get_user_db
from core.authentication.user_manager import UserManager
from fastapi import Depends

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    user_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_user_db),
    ],
):
    yield UserManager(user_db)
