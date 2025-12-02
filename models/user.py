from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

class UserCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
