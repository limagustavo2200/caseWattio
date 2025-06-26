from models.movie import Movie
from ports.movie_interface import MovieInterface

class UpdateMovie:
    def __init__(self, repo: MovieInterface):
        self.repo = repo

    def execute(self, movie: Movie) -> None:
        self.repo.update(movie)