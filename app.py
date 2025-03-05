from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()
DATA_FILE = "data.json"



class Item(BaseModel):
    name: str
    price: float

def read_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.get("/items")
def get_items():
    return read_data()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    items = read_data()
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items")
def create_item(item: Item):
    items = read_data()
    new_item = {"id": max(i["id"] for i in items) + 1 if items else 1, **item.dict()}
    items.append(new_item)
    write_data(items)
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    items = read_data()
    for item in items:
        if item["id"] == item_id:
            item["name"] = updated_item.name
            item["price"] = updated_item.price
            write_data(items)
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    items = read_data()
    filtered_items = [i for i in items if i["id"] != item_id]

    if len(items) == len(filtered_items):
        raise HTTPException(status_code=404, detail="Item not found")

    write_data(filtered_items)
    return {"message": "Item deleted"}
