from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


app = FastAPI()


# @app.get("/")
# def index():
#     return {"data": "blog list"}


@app.get("/blog")
def show(limit: int= 15, published: bool= True, sort: Optional[str] = None):
    # only get 10 published blogs
    # sort: sắp xếp lại danh sách hiện thị
    if published:
        return {"data": f"{limit} of published blogs from the database"}
    else:
        return {"data": f"{limit} of blogs from the database"}


@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/command")
def show(id: int, limit: int= 10): 
    return {"data" : {"1", "2"}}


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host= "127.0.0.1", port= 9000)