from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    id: int
    produto: str
    price: float
    qtde: int



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/produtos")
def read_item(id: int):
    return {"ID do produto": id, "produto": Item.produto, "preço": Item.price, "quantidade": Item.qtde}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):

    return {"item_name": item.name, "item_id": item_id}
