from redis_om import HashModel
from app.db.redis.redis_core import redis_db

class Task(HashModel):
    name: str
    description: str

    class Meta:
        database: redis_db
    


def format(pk:str):
    _task = Task.get(pk)
    return {
        "id":_task.pk,
        "name": _task.name,
        "description":_task.description
    }