from fastapi import APIRouter
from src.app.dependencies import UrlServiceDep
from src.app.utils import handle_business_errors

router = APIRouter(tags=["Tracking"], prefix="/track")


@router.get("/info/{alias}", summary="Get url info by alias")
@handle_business_errors
async def get_url_info(alias: str, service: UrlServiceDep):
    return await service.get_info(alias)


@router.get("/all", summary="Get all urls")
async def get_all_urls(service: UrlServiceDep):
    return await service.get_all()
