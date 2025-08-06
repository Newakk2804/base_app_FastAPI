from fastapi.security import HTTPBearer
from api.api_v1.auth import router as auth_router
from api.api_v1.users import router as users_router
from core.config import settings
from fastapi import APIRouter, Depends

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(prefix=settings.api.v1.prefix, dependencies=[Depends(http_bearer)])

router.include_router(auth_router)
router.include_router(users_router)
