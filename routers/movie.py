from typing import Optional

from fastapi import APIRouter, Depends, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from schemas.movie import Movie
from services.movie import MovieService

movie_router = APIRouter()


# Movies
@movie_router.get(
    "/movies", tags=["movies"], status_code=200, dependencies=[Depends(JWTBearer())]
)
def message(category: str = None):
    if category:
        db = Session()
        data = MovieService(db).get_movies_by_category(category)
        if data:
            return JSONResponse(jsonable_encoder(data), status_code=200)
        return JSONResponse({"error": "There aren't movies with that category"})
    db = Session()
    data = db.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(data))


@movie_router.get(
    "/movies/{id}",
    tags=["movies"],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies_by_id(id: int = Path(le=2000, ge=1)):
    db = Session()
    data = MovieService(db).get_movies_by_id(id)
    if data:
        return JSONResponse(jsonable_encoder(data))
    return JSONResponse({"error": "Movie not found"}, status_code=400)


@movie_router.post(
    "/movies/", tags=["movies"], status_code=201, dependencies=[Depends(JWTBearer())]
)
def create_movies(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "The movie has been created successfully"})


@movie_router.put(
    "/movies/{id}",
    tags=["movies"],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def update_movies(id, movie: Movie):
    db = Session()
    result = MovieService(db).get_movies_by_id(id)
    if result:
        MovieService(db).update_movie(id, movie)
        return JSONResponse({"message": "The movie has been updated successfully"})
    return JSONResponse({"message": "Movie not found"})


@movie_router.delete(
    "/movies/{id}",
    tags=["movies"],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def delete_movie(id):
    db = Session()
    result = MovieService(db).get_movies_by_id(id)
    if result:
        MovieService(db).delete_movie(id)
        return JSONResponse({"message": "The movie has been deleted successfully"})
    return JSONResponse({"message": "Movie not found"})
