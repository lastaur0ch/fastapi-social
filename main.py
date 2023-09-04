from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "favourite food", "content": "fufu and egusi", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"response": "Post created successfully", "data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with ID: {id} was not found. Try a different ID")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with ID: {id} was not found. Try a dfferent ID"}
    return {"post_detail": post}

