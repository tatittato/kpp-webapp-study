from fastapi import APIRouter

router = APIRouter(
    tags=["Rank"],
    responses={404: {"description": "Not found"}},
)


@router.get("/rank/list")
async def get_rank_list():
    pass


@router.post("/rank/score")
async def save_score():
    pass
