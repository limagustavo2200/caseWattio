from models.movie import Movie
from ports.movie_repository import MovieRepository


class ListMovie:
    def __init__(self, repo: MovieRepository):
        self.repo = repo

    def execute(self) -> list[Movie]:
        return self.repo.list()