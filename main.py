
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/mahasiswa/{nim}")
def ambil_mhs(nim:str):
 return {"nama": "Budi Martami"}