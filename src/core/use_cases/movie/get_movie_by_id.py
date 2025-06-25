from models.movie import Movie
from ports.movie_repository import MovieRepository


class GetMovieById:
    def __init__(self, repo: MovieRepository):
        self.repo = repo

    def execute(self, movie_id: int) -> Movie | None:
        return self.repo.get_by_id(movie_id)