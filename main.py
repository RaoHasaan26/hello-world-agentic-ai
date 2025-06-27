from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None ):
    return {"item_id": item_id, "query": q}

@app.post("/create")
def create_item(data: dict):
    return {"message": "received","data": data}
