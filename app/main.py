from fastapi import FastAPI
from .routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"msg": "Sistema de Inventarios listo 🔥"}
