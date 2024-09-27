from fastapi import APIRouter
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from new_app.backend.db import Base

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_tasks():
    pass


@router.get("/{task_id}")
async def task_by_id():
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass

