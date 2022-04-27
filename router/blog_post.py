from fastapi import APIRouter, status, Response


router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post("/new")
def create_blog():
    return {"message": "new post created"}