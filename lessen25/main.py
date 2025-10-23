from fastapi import FastAPI ,HTTPException
from typing import List
import database
import models
from models import Movecreate, Movie

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "wellcome to crud "}

