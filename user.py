from fastapi import APIRouter
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from new_app.backend.db import Base


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_users():
    pass


@router.get("/{user_id}")
async def user_by_id():
    pass


@router.post("/create")
async def create_user():
    pass


@router.put("/update")
async def update_user():
    pass


@router.delete("/delete")
async def delete_user():
    pass

