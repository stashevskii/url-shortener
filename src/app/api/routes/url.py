from fastapi import APIRouter, Depends
from src.app.dependencies import UrlServiceDep
from src.app.schemas import ExternalLink
from src.app.utils import handle_business_errors

router = APIRouter(tags=["Urls"])


@router.get("/{alias}", summary="Redirect to original url by alias")
@handle_business_errors
async def get_url(alias: str, service: UrlServiceDep):
    return await service.get(alias)


@router.post("/shorten", summary="Get alias by url")
@handle_business_errors
async def add_url(service: UrlServiceDep, schema: ExternalLink = Depends()):
    return await service.add(schema)
