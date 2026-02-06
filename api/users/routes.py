from fastapi import APIRouter, Query

user_router = APIRouter("/users", tags=["users"])

@user_router.get(
    "/{user_id}"
)
async def get_user(

):
    ...

@user_router.get(
    "/"
)
async def get_users(

):
    ...

@user_router.post(
    "/"
)
async def create_user(

):
    ...

@user_router.patch(
    "/{user_id}"
)
async def update_user(
    
):
    ...