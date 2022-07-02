from fastapi import FastAPI

from api.summary import summary_api

app = FastAPI()


app.include_router(summary_api.router)
