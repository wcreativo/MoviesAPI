from fastapi import FastAPI

from config.database import Base, engine
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)
