from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_article
from schemas import ArticleBase, ArticleDisplay
from db.database import get_db


router = APIRouter(prefix="/article", tags=["Article"])


# Create User
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# get a specific article
@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
