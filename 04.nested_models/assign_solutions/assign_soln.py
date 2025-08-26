from pydantic import BaseModel
from typing import List ,Optional

class Lesson(BaseModel):
    title:str
    content:str

class Module(BaseModel):
    name:str
    duration_in_hours:float
    chapter:List[Lesson]

class Course(BaseModel):
    title:str
    description:str
    instructor:Optional[str]
    modules : List[Module]