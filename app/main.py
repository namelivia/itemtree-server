from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.items.api import router as items
from app.images.api import router as images
from app.users.api import router as users
from app.comments.api import router as comments
import logging
import sys

app = FastAPI()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

origins = ["http://localhost:3000", "http://expenses.namelivia.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

[
    app.include_router(router)
    for router in [
        items,
        images,
        users,
        comments,
    ]
]
