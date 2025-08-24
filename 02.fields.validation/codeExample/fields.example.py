from pydantic import BaseModel #type:ignore
from typing import Optional ,List ,Dict 

#creating the cart model 
class Cart_model(BaseModel):
    user_id : int 
    items: List[str]
    quantity : List[Dict[str, int]]#array of the dictionary which has the name of the item and the quantity


#creating the blog post model to explore the Blog_post_model
class Blog_post_model(BaseModel):
    title:str
    content:str
    image_url : Optional[str] = None #mnaking this an optional field


