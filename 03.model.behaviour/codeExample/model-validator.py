#here we are going to learn about the model validator and feild-validator
from pydantic import BaseModel,Field , field_validator,model_validator,computed_field

#writing the customised validator for each field - its a decorator 

#understanding the feild-validator
class User(BaseModel):
    username: str

    #it takes the value fo the class which we refer using cls , and the value (v) -which in our case is username
    @field_validator('username')
    def username_validation(cls,v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return v
    


#understanding modelValidator
class SignupData(BaseModel):
    password:str
    confirm_password:str

    #here we are implementing the custom validator for whole model so it takes to things - one the class and the second thing it takes is the value
    # here is a concept of mode which is either after or before so 
    '''
    if we choose after mode = it will validate after we get all the values 
    if we choose before mode = it will validate before we get all the values
    '''
    @model_validator(mode="after")
    def pass_validator(cls , values):
        if values.password != values.confirm_password:
            raise ValueError("passwords don't match")
        return values
    

#understanding  using product_model
class Product(BaseModel):
    price:float
    quantity:int

#here we are understanding the computed fields- which is used to make a property so computed_field decorator takes inside a decorator

    @computed_field
    @property
    def total_price(self)->float:
        return self.price*self.quantity