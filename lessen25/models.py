from pydantic import BaseModel

class Movecreate(BaseModel):
    tittle: str
    description: str


class Movie(BaseModel): 
      id: int

