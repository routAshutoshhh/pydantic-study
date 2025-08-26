from pydantic import BaseModel
from typing import List ,Optional


class Address(BaseModel):
    street:str
    City:str
    postal_code:str


class User(BaseModel):
    id:int
    name:str
    address: Address #nested model referencing
    


#this is also called forward referencing
class Comment(BaseModel):
    id:int
    content:str
    repliesToComment:Optional[List['Comment']] = None #here the replies is self-referencing the comment itself


#whenever you have a model that references itself, you need to use a string literal to avoid issues with forward references
#then we need to do the rebuild with the classsName
Comment.model_rebuild()


#lets create  the object for the  classes to understand the things more clearly
add = Address(
    street ="park street main road",
    City ="Kolkata",
    postal_code ="700001"
)

#understanding the referencing to other model
userFromKolkata = User(
    id=1,
    name= "Bengali chele",
    address = add
)

#lets understand the object creating for the referecing model to own model
commentsFromReddit  = Comment(
    id=1,
    content ="hello first from the blog",
    repliesToComment =[
        Comment(id=1,
                content="first reply to first comment"
                ),
        Comment(id=2,
                content="second reply to first comment"
                )
    ]
)