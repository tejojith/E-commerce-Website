from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import model, schemas, database 

router = APIRouter(
    prefix = "/products",
    tags = ['Products'] )



#get all products

@router.get("/")
def get_products(db: Session = Depends(database.get_db)):
 
    product = db.query(model.Product).all()
    return product

#create a new product

@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.Product)
def create_products(post: schemas.ProductCreate, db: Session = Depends(database.get_db)):

    new_product = model.Product(**post.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

#delete a product

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT )
def delete_product(id: int,db: Session = Depends(database.get_db)):

    product_query = db.query(model.Product).filter(model.Product.id == id)

    product = product_query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post of id{id} doesnt exist")
    
    # if product.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "NOT authorised to perform req action")
   
    product_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)


#update a product
@router.put("/{id}", response_model=schemas.Product)
def update_product(id: int, updated_post: schemas.ProductCreate,db: Session = Depends(database.get_db)):

    product_query = db.query(model.Product).filter(model.Product.id == id)
    product = product_query.first()


    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post of id{id} doesnt exist")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "NOT authorised to perform req action")

    product_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return product_query.first()
    















#     ---------
    #cursor.execute("""SELECT * FROM post """)
    #posts = cursor.fetchall()
    # print(limit)

    # posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()

    # results = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(model.Vote, model.Post.id == model.Vote.user_id, isouter=True).group_by(model.Post.id).filter(
    #     model.Post.title.contains(search)).limit(limit).offset(skip).all()



    # return results