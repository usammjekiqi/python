from pydentic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, )