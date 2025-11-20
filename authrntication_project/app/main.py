from fastapi import FastAPI, HTTPException, Depends
from typing import List
from crudc import create_item, get_item, get_items, update_item, delete_item
from modelsc import item
from pip import get_api_key
from databasec import init_db

app = FastAPI()
init_db()

@app.post("/items/", response_model=item)
def create_new_item(item_data: item, api_key: str = Depends(get_api_key)):
    return create_item(item_data)

@app.get("/items/", response_model=List[item])
def read_items(api_key: str = Depends(get_api_key)):
    return get_items()

@app.get("/items/{item_id}", response_model=item)
def read_item(item_id: int, api_key: str = Depends(get_api_key)):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=item)
def update_existing_item(item_id: int, item_data: item, api_key: str = Depends(get_api_key)):
    updated_item = update_item(item_id, item_data)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
def delete_existing_item(item_id: int, api_key: str = Depends(get_api_key)):
    result = delete_item(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted successfully"} 