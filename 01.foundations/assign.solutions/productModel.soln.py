from pydantic import BaseModel #type:ignore
#creating a classs  which is the model for the Product 
class Product_model(BaseModel):
    id: int
    name: str 
    price: float
    in_stock: bool