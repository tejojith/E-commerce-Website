from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import model, schemas, util, oauth2
from .. import database 

router = APIRouter(
    prefix = "/products",
    tags = ['Products'] )


@router.get("/")
def get_products(db: Session = Depends(database.get_db)):
    
    
    #cursor.execute("""SELECT * FROM post """)
    #posts = cursor.fetchall()
    # print(limit)

    # posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()

    # results = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote, model.Post.id == model.Vote.user_id, isouter=True).group_by(model.Post.id).filter(
    #     model.Post.title.contains(search)).limit(limit).offset(skip).all()



    # return results