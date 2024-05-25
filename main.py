from turtle import pos
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    description: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello ji ki haal chaal"}

@app.get("/posts")
async def get_posts():
    return {"data": "this is a post"}

@app.post("/createposts")
async def create_post(posts: Post):
    print(f"Post title: {posts.title}")
    print(f"Post content: {posts.description}")
    print(f"Post published: {posts.published}")
    print(f"Post rating: {posts.rating}")
    return {"data": "post sent to server"}
