from fastapi import APIRouter

router = APIRouter(
    tags=["Speech"],
    responses={404: {"description": "Not found"}},
)


@router.post("/speech/score")
async def get_score():
    pass
