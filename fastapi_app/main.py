from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI

from .routers import rank, speech

from .views import home, ranking

tags_metadata = [
    {
        "name": "Rank",
        "description": "발음 랭킹 관련 API",
    },
    {
        "name": "Speech",
        "description": "음성처리 관련 API",
    },
    {
        "name": "Web Pages",
        "description": "웹 페이지 (API 아님)",
    }
]
app = FastAPI(openapi_tags=tags_metadata, title="api", version="0.0.1", )

routers = [home, ranking, rank, speech]
for r in routers:
    app.include_router(r.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
