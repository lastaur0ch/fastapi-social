from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#define the response model data. Can inherit from PostBase and present only additional fields
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True