from fastapi import FastAPI

from api import summary

app = FastAPI()


app.include_router(summary.router)
