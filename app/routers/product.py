from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import model, schemas, database 

router = APIRouter(
    prefix = "",
    tags = ['Products'] )




@router.get("/products/")
def get_products(db: Session = Depends(database.get_db)):
 
    product = db.query(model.Product).all()
    return product


@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.Product)
def create_products(post: schemas.ProductCreate, db: Session = Depends(database.get_db)):

    new_product = model.Product(owner_id = id,**post.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product








#     ---------
    #cursor.execute("""SELECT * FROM post """)
    #posts = cursor.fetchall()
    # print(limit)

    # posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()

    # results = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote, model.Post.id == model.Vote.user_id, isouter=True).group_by(model.Post.id).filter(
    #     model.Post.title.contains(search)).limit(limit).offset(skip).all()



    # return results