from fastapi import APIRouter, Depends
from app.schemas import SampleRequest, SampleResponse
from app.services import SampleService
from app.settings import get_settings

router = APIRouter(prefix="/api")

@router.post("/sample", response_model=SampleResponse)
async def post_sample(
    payload: SampleRequest,
    service: SampleService = Depends(),
):
    """
    Thin route handler using DI for business logic.
    """
    result = await service.process(payload)
    return result

def register_routes(app):
    """
    Registers all routers with the main FastAPI app.
    """
    app.include_router(router)
