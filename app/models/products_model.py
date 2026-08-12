from pydantic import BaseModel

class ProductsModel(BaseModel):
    id:int
    name:str
    description:str | None = None
    price:float
    stock:int
    category:str | None = None