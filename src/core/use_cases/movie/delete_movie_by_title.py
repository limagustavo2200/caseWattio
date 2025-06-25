from models.movie import Movie
from ports.movie_repository import MovieRepository


class DeleteMovieByTitle:
    def __init__(self, repo: MovieRepository):
        self.repo = repo

    def execute(self, title: str) -> None:
        movie = self.repo.get_by_title(title)
        if movie:
            self.repo.delete(movie)
        else:
            raise ValueError(f"O filme '{title}' não foi encontrado. Verifique o título e tente novamente.")