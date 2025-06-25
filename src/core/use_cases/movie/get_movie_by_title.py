from models.movie import Movie
from ports.movie_repository import MovieRepository


class GetMovieByTitle:
    def __init__(self, repo: MovieRepository):
        self.repo = repo

    def execute(self, title: str) -> Movie | None:
        return self.repo.get_by_title(title)