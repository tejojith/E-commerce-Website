from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import time
# from . import database,schemas, model
# from .routers import post, user, auth, vote
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


# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)
# app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "hello world"}


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

