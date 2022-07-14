#
# from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
#
# app = FastAPI() # gọi constructor và gán vào biến app
#
# @app.get("/") # giống flask, khai báo phương thức get và url
# def root():
#     return {"Hello World"}

# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/items/")
# def read_item(name: str, address: str):
#     return [{"name": name}, {"address": address}]

from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Infor(BaseModel):
    name: str
    address: str

app = FastAPI()

@app.post("/") #
def create_item(infor: Infor):
    return infor



