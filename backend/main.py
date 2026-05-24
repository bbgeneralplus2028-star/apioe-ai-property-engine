from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="APIOE Property AI Engine")

app.include_router(router)

@app.get("/")
def home():
    return {"status": "APIOE running"}
