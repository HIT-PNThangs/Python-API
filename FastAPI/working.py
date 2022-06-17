from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# request Get method url: "/"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def get():
    return {"message": "Hello world!"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createsposts") 
def post_posts(post: Post):
    return {"data": post.dict()}