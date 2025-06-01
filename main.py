from fastapi import FastAPI

import dotenv
dotenv.load_dotenv(".env")

from routes import base

app = FastAPI()
app.include_router(base.base_router)