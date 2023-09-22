from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#define the response model data. Can inherit from BaseModel and specify all fields to be sent to FE
#here I inherited PostBase so all its properties must the shown and the additional ones I stated
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True