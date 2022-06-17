from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel): # kế thừa BaseModel
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# @app.get("/about")
# def about():
#     return {"Data" : "About"}

inventory = {
        1: {
            "name" : "Milk",
            "price" : 3.99,
            "brand": "Regular"
        }
    }

# truỳen url vào dạng
# http://127.0.0.1:8000/get_item/1
@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(None, description= "The ID of the item you like", gt= 0)):
    return inventory[item_id]

# # truyền url vào dạng
# # http://127.0.0.1:8000/get_by_name?name=Milk
# @app.get("/get_by_name") 
# def get_item(name: str):
#     for item_id in inventory:
#         if inventory[item_id]['name'] == name:
#             return inventory[item_id]

#     return {"Data" : "Not found"}

# #http://127.0.0.1:8000/get_by_name?name=Milk&test=2 
# @app.get("/get_by_name") 
# def get_item(*, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]['name'] == name:
#             return inventory[item_id]

#     return {"Data" : "Not found"}


#http://127.0.0.1:8000/get_by_name?name=Milk&test=2 
@app.get("/get_by_name") 
def get_item(nam: str = Query(None, title= 'name', description= "abc", max_length= 10, min_length= 2)):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]

    raise HTTPException(status_code= 404, detail= "Item name not found.")


# # http://127.0.0.1:8000/get_by_name/1?name=Milk&test=1
# @app.get("/get_by_name/{item_id}") 
# def get_item(*, item_id: int, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]['name'] == name:
#             return inventory[item_id]

#     return {"Data" : "Not found"}


@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code= 400, detail= 'Item ID already exists')

    inventory[item_id] = {"name": item.name, "price" : item.price, "brand": item.brand}
    return inventory[item_id]


@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error" : "Item ID does not exists"}

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete_item")
def delete_item(item_id: int = Query(..., description= "The ID ...")):
    if item_id not in inventory:
        raise HTTPException(status_code= 404, detail= "Item name not found.")

    del inventory[item_id]
    return {"Success": "ID does not exists"}