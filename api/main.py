from fastapi import FastAPI
from api.middleware import setup_middleware
from api.routes import router

app = FastAPI(
    title="MatchDay Agent API",
    description="API for the World Cup 2026 match-day planning assistant",
    version="1.0.0",
)

setup_middleware(app)
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    from config.settings import settings
    uvicorn.run("api.main:app", host=settings.HOST, port=settings.PORT, reload=True)
