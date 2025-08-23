from pydantic import BaseModel


#creating class which is basically the model
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active:bool 


#creating input_data
input_data = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "is_active": True
}

#so now we need to create a user which should be of User class
user = User(**input_data)  #unpacking the input_data dictionarys
print(user)