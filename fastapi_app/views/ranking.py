from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=["Web Pages"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")


@router.get("/ranking", response_class=HTMLResponse)
async def ranking_page(request: Request):
    return templates.TemplateResponse(
        "ranking.html",
        {
            "request": request,
            "test_text": "hello ranking page"
        })
