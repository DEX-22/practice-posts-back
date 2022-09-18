from fastapi import APIRouter
from config.db import connectMysql
from uuid import uuid4 as uuid
from models.post import posts
from schemas.post import Post
from sqlalchemy import desc

post = APIRouter()

@post.get("/posts")
def get_posts():
    return connectMysql.execute(posts.select().order_by(desc(posts.c.created_at))).fetchall()


@post.get("/posts/{id}")
def get_post(id: str):
    searchPost = connectMysql.execute(posts.select().where(posts.c.id == id)).first()

    if searchPost:
        return searchPost

    return "post not found"


@post.post("/posts")
def insert_post(post: Post):
    post.id = uuid()
    res = connectMysql.execute(posts.insert().values(post.dict()))

    return res


@post.put("/posts/{id}")
def update_post(id: str, post: Post):
    connectMysql.execute(
        posts.update().values(content=post.content).where(posts.c.id == id)
    )


@post.delete("/posts/{id}")
def delete_post(id: str):
    postDeleted = connectMysql.execute(posts.delete().where(posts.c.id == id))
    return "deleted"
