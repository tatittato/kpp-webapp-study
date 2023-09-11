from fastapi import APIRouter

router = APIRouter(
    tags=["test"],
    responses={404: {"description": "Not found"}},
)


@router.get("/test")
async def get_rank_list():
    
    return "test"
