from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.post import post

app = FastAPI()

origins = [
    'localhost:5173',
    'localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # allow_origins=origins,
    # allow_credentials=False,
    allow_methods=['GET','POST','PUT','PATCH','DELETE'],
    allow_headers=['Origin', 'Content-Type','X-Requested-With']
)

app.include_router(post)
