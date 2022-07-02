from fastapi import FastAPI

from src.api import summary

app = FastAPI()


app.include_router(summary.router)
