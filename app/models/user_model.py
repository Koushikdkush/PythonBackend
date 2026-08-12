from pydantic import BaseModel

class UserModel(BaseModel):
    id:int
    name:str
    email:str
    age:int | None = None
    address:str | None = None
    skills:list[str] | None = None