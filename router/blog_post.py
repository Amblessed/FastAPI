from importlib.metadata import metadata
from typing import Dict, List
from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel


router = APIRouter(prefix="/blog", tags=["Blog"])


class Image(BaseModel):
    url: str
    alias: str


# This defines the format for the request body of the post.
class BlogModel(BaseModel):
    title: str
    content: str 
    number_comments: int
    published: bool | None
    tags: List[str] = []
    metadata: Dict[str, str] = {"Key1": "value1"}
    image: Image | None = None
   


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "Blog": blog, "version": version}


 # Body(...) or Body(Ellipsis) --> Non optional parameter. 
@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None, title="Title of the comment", description="Description for the comment title", alias="commentId", deprecated=True), content: str=Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
                   v: List[str] | None = Query(["1.0", "1.1", "1.2"]), comment_id: int = Path(None, gt=5, le=10)):
    return {"id": id, "Blog": blog, "comment_title": comment_title, "content": content, "version": v, "comment_id": comment_id}




def required_functionality():
    return {"message": "learning fastapi is important"}
