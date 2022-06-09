from imp import reload
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from app.routes.route_redis import router as redis_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def hello_check():
    return {
        "project name":"Redis CRUD",
        "project version": "v0.0.0"
    }


app.include_router(
    redis_router,
    prefix="/api/v1/task",
    tags=["Redis CRUD Management"]
)




if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
        reload=True,
        # log_level= "debug",
        access_log=False,
        use_colors=True
    )