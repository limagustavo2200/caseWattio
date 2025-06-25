from abc import ABC, abstractmethod
from models.movie import Movie
from typing import List, Optional

class MovieRepository(ABC):
    @abstractmethod
    def add(self, movie: Movie) -> None:
        pass
    
    @abstractmethod
    def list(self) -> List[Movie]: 
        pass
                
    @abstractmethod
    def get_by_id(self, movie_id: int) -> Optional[Movie]:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Movie]:
        pass
    
    @abstractmethod
    def delete_by_title(self, title: str) -> None:
        pass