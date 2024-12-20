from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, vehicles

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Vehicle Marketplace!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(vehicles.router)