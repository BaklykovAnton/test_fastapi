from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Program(BaseModel):
    id : int
    user_id: int
    file_name : str
    text : str

class User(BaseModel):
    id : int
    name : str

@app.get("/")
def hello():
    return 'hello'

sources: List[Program] = [ 
        Program(id = 1, user_id = 1, file_name = "test1", text = "print('Hello world')"), 
        Program(id = 2, user_id = 1, file_name = "test2", text = "print(1+2)")
    ]

fake_users = [
    {"id" : 1, "name" : "Anton"},
    {"id" : 2, "name" : "Ivan"}
]

@app.get("/users/{user_id}", response_model = User)
def get_user(user_id : int):
    return [(user.get("id"), user.get("name")) for user in fake_users if user.get("id") == user_id]

@app.get("/users/{user_id}/sources", response_model = List[Program])
def get_sources(user_id : int, limit :int = 1, offset : int = 0):
    res = list(filter(lambda x : x.user_id == user_id, sources))
    return res[offset:][:limit]


@app.post("/users/")
def add_program(program : Program):
    sources.append(program)
    return {"status" : 200,  "data" : sources}