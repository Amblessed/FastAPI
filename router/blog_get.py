from fastapi import APIRouter, Depends, status, Response
from enum import Enum

from router.blog_post import required_functionality


router = APIRouter(prefix="/blog", tags=["Blog"])


#The order is important in the execution and goes from top to down
@router.get("/all", summary="Retrieve all blogs",
         description="This api call stimulates fetching all blogs",
         response_description="List of all available blogs")
# page_size is an optional parameter
def get_all_blogs(page: int = 1, page_size: int | None = None, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}", "required": req_parameter}


@router.get("/{id}/comment/{comment_id}", tags=["Comment"], summary="Retrieves a Comment")
def get_comment(id: int, comment_id: int, valid: bool = True, username: str | None = None):
    """
    Simulates retrieving a comment of a blog
    - **id**: mandatory path parameter
    - **comment**: mandatory path parameter
    - **valid**: optional query parameter
    - **username**: optional query parameter
    """
    return {"message": f"Blog with id {id}, comment with id {comment_id}, valid {valid} and username is {username}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")      # Predefined values
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


# {id} is a path parameter
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Blog with id {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}
