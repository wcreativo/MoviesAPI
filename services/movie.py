from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        data = self.db.query(MovieModel).all()
        return data

    def get_movies_by_id(self, id):
        data = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return data

    def get_movies_by_category(self, category):
        data = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return data

    def create_movie(self, movie: Movie):
        movie = MovieModel(**movie.dict())
        self.db.add(movie)
        self.db.commit()
        return

    def update_movie(self, id, movie: Movie):
        result = self.get_movies_by_id(id)
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        return

    def delete_movie(self, id):
        movie = self.get_movies_by_id(id)
        self.db.delete(movie)
        self.db.commit()
        return
