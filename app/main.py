# app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Dartañan!"}

@app.get("/prueba_manuel")
def read_root():
    # GENERATE CHANGES HERE TO PROVE SYNC STAGE
    return {"message": "Hello, Manuel!"}