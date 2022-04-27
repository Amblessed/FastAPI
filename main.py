from enum import Enum
from fastapi import FastAPI

app = FastAPI()               #Instantiate an object of the FastAPI class

@app.get("/")
def index():
    return {"message":"Hello World!"}


# @app.get("/blog/all")     # {id} is a path parameter
# def get_all_blogs():
#     return {"message": "All blogs provided"}

#The order is important in the execution and goes from top to down
@app.get("/blog/all") 
def get_all_blogs(page: int = 1, page_size: int | None = None):     # page_size is an optional parameter
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comment/{comment_id}") 
def get_comment(id: int, comment_id: int, valid: bool = True, username: str | None = None):
    return {"message": f"Blog with id {id}, comment with id {comment_id}, valid {valid} and username is {username}"}

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}")      # Predefined values
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@app.get("/blog/{id}")     # {id} is a path parameter
def get_blog(id: int):
    return {"message":f"Blog with id {id}"}