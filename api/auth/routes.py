from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get(
    "/api_key"
)
async def get_api_key(

):
    ...