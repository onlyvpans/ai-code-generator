# set up fastAPI application
# fastAPI = api framework that allows us to make an API in python

import os

from clerk_backend_api import Clerk
# from clerk import Client as ClerkClient
from fastapi import FastAPI, Request, Response

# cors - makes sure we can send info from frontend to backedn
from fastapi.middleware.cors import CORSMiddleware

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))
# clerk_sdk = ClerkClient(token=os.getenv("CLERK_SECRET_KEY", ""))
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
