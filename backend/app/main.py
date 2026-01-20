from fastapi import FastAPI
from app.api.routes import search  # <-- THIS WAS MISSING

app = FastAPI(title="Credisearch API")

app.include_router(search.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
