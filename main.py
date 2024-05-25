from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    description: str

@app.get("/")
async def root():
    return {"message": "Hello ji ki haal chaal"}

@app.get("/posts")
async def get_posts():
    return {"data": "this is a post"}

@app.post("/createposts")
async def create_post(posts: Post):
    print(posts)
    return {"data": "post sent to server"}
