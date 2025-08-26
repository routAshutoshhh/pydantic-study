'''
📌 Serialization (plain English)

Serialization = taking an in-memory Python object (like a User model with datetime, dict, list, etc.) and converting it into a format that can be stored or transmitted (like JSON, string, bytes).

Think of it as:
👉 “Packaging your object so it can leave Python-land and travel somewhere else.”

The reverse process is called deserialization.
'''

from pydantic import BaseModel ,ConfigDict,field_serializer
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str


class User(BaseModel):
    id:int
    name:str
    email:str
    address:Address
    isActive:bool = True
    createdAt:datetime
    tags : List[str]=[]

    #we want to configure the datetime look using the configDict
    model_config = ConfigDict(
        #here we will need to create the custom encoders for the datetime field
        json_encoders = {
            datetime: lambda v:v.strftime("%Y-%m-%d %H:%M:%S")
        }
    )

        # ✅ field-level serializer for datetime - alternative approach
    # @field_serializer("createdAt")
    # def serialize_created_at(self, value: datetime, _info):
    #     return value.strftime("%Y-%m-%d %H:%M:%S")

    


#creating a uiser instance
user1 = User(
    id =1,
    name = "John Doe",
    email = "john.doe@example.com",
    address = Address(
        street = "123 Main St",
        city = "Anytown",
        zip_code = "12345"
    ),
    isActive = True,
    createdAt = datetime(2025,3,15,14,30),
    tags = ["user", "admin"]
)


#using model_dump() to understand the output and the serialization process
#using model_dump() - expected output should be dictionary (model_dump()->dict)
pythn_model_dict = user1.model_dump()
print(pythn_model_dict)

print("\n")
#json serialization using model_dump_json()
python_model_json = user1.model_dump_json()
print(python_model_json)



#code for deserialization
"""
data = '{"id": 1, "name": "John"}'
user2 = User.model_validate_json(data)
print(user2)  # → User(id=1, name='John')

"""