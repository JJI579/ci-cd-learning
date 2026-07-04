from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="CI CD Learning")

names = [x.strip() for x in open('names.txt').readlines()]

# Adding CORS to allow cross-origin requests


origins = ["*"]  # List of allowed origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def index():
	return {
		"text": f"Hello {random.choice(names)}!"
	}

