from api.api_v1.auth import router as auth_router
from api.api_v1.users import router as users_router
from core.config import settings
from fastapi import APIRouter

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(auth_router)
router.include_router(users_router)
