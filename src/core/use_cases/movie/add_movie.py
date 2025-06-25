from models.movie import Movie
from ports.movie_repository import MovieRepository

class AddMovie:
    def __init__(self, repo: MovieRepository):
        self.repo = repo

    def execute(self, movie: Movie) -> None:
        self.repo.add(movie)