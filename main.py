from turtle import pos
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    description: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "Hello", "content": "example", "id": 1}, {"title": "Hello-1", "content": "example-1", "id": 2}]

@app.get("/")
async def root():
    return {"message": "Hello ji ki haal chaal"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
async def create_post(posts: Post):
    # print(f"Post title: {posts.title}")
    # print(f"Post content: {posts.description}")
    # print(f"Post published: {posts.published}")
    # print(f"Post rating: {posts.rating}")
    # print(posts.model_dump())

    post_dict = posts.model_dump()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
