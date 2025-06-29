from fastapi import FastAPI
from fetch_gs import fetch_data
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    fetch_data()
    return {"message": "Hello, World!"}

#if __name__ == "__main__":
#    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)