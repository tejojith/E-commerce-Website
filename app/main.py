from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import database, model
from .routers import product
from sqlalchemy.orm import Session
# from .config import settings

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model.Base.metadata.create_all(bind=database.engine)


app.include_router(product.router)
# app.include_router(user.router)
# app.include_router(auth.router)
# app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "hello world, this is a new project"}

# @app.get("/products/")
# def get_products(db: Session = Depends(database.get_db)):
 
#     product = db.query(model.Product).all()
#     return product



while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'ecommerce', user = 'postgres', password = 'password1234', cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print("database connection was success")
        break
    except Exception as error:
        print("connecting to database failed")
        print("error: ", error)
        time.sleep(2)

