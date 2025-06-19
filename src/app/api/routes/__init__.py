from fastapi import APIRouter, FastAPI
from .health import router as health_router
from .track import router as admin_router
from .url import router as url_router

router = APIRouter()
router.include_router(health_router)
router.include_router(admin_router)
router.include_router(url_router)


def register_main_router(app: FastAPI) -> None:
    app.include_router(router)


__all__ = ["register_main_router"]
