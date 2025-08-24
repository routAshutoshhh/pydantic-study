from pydantic import BaseModel , Field
from typing import Optional
"""
context before the understanding of the implementation 
Field can be used to define the validation constraints for  the pydantic model 
Field(...) = required field - just some weird syntax
min_length = minimum length of string field
max_length = maximum length of string field
min_value = minimum value of numeric field
max_value = maximum value of numeric field
description = description of the field
example = example of the field
ge = means greater than or equal to the value specified
"""



class Employee_model(BaseModel):
    id:int  = Field(... ,min_length=3 , max_length=50, description= "the employee Id with unique values")
    name:str = Field(...,min_length=3 , max_length=50, description="the name of the employee",examples=["Ashutosh Kumar Rout"])
    department:Optional[str] = 'General'
    salary:float = Field(...,  ge = 100000)