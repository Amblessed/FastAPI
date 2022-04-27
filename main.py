from enum import Enum
from fastapi import FastAPI, status, Response

app = FastAPI()               #Instantiate an object of the FastAPI class

@app.get("/hello")
def index():
    return {"message":"Hello World!"}


#The order is important in the execution and goes from top to down
@app.get("/blog/all", tags= ["blog"], summary="Retrieve all blogs", 
        description="This api call stimulates fetching all blogs", 
        response_description= "List of all available blogs") 
def get_all_blogs(page: int = 1, page_size: int | None = None):     # page_size is an optional parameter
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comment/{comment_id}", tags=["blog", "comments"], summary="Retrieves a Comment") 
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


@app.get("/blog/type/{type}", tags=["blog"])      # Predefined values
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


# {id} is a path parameter
@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Blog with id {id} not found"}
    else:
        return {"message":f"Blog with id {id}"}
