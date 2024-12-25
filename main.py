import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import auth, vehicles, posts, me

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Vehicle Marketplace Web Application",
        "documentation_url": "/docs"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/media", StaticFiles(directory=os.path.join(os.getcwd(), "media")), name="media")

app.include_router(auth.router)
app.include_router(me.router)
app.include_router(vehicles.router)
app.include_router(posts.router)
