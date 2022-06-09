from fastapi import APIRouter
from app.schemas.schema_redis import Task,format

router = APIRouter()

@router.post("/")
async def create(task: Task):
    return task.save()


@router.get("/")
async def read():
    return [format(pk) for pk in Task.all_pks()]


@router.put("/{pk}")
async def update(
    pk:str,
    task:Task
):
    _task = Task.get(pk)
    _task.name = task.name
    _task.description = task.description
    return _task.save()


@router.delete("/{pk}")
async def delete(pk:str):
    _task = Task.get(pk)
    return _task.delete(pk)