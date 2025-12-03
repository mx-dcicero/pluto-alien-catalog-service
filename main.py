from fastapi import FastAPI
from routes.aliens import router as aliens_router

app = FastAPI(title="Pluto Alien Catalog Service")

# Attach the alien-related endpoints
app.include_router(aliens_router)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
