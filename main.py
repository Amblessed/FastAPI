from fastapi import HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi import FastAPI, Request
from exceptions import StoryException
from router import blog_get, blog_post, user, article, product, file
from auth import authentication
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# Instantiate an object of the FastAPI class
app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World!"}


@app.exception_handler(StoryException)
def story_exception(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={'detail': exc.name})


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount('/files', StaticFiles(directory='files'), name='files')
