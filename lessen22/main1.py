from pydantic import BaseModel, V alidationInfo, field_validator, constr, conint

# class User(BaseModel):
#     id: int
#     name: str
#     age: int

#     @field_validator('age')
#     def must_be_positive(cls, v, info: ValidationInfo):
#         if v <= 0:
#             raise ValueError('Age must be a positive integer')
#         return v
    
# try:
#     user = User(id=1, name="John Doe", age=-1)
# except ValueError as e:
#     print(e)

class Address(BaseModel):
    street: str
    city: str
    
class another_User(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)
