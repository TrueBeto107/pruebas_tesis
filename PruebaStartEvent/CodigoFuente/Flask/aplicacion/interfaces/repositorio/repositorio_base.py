from abc import ABC, abstractmethod
from typing import TypeVar,  Generic

T = TypeVar('T')

class RepositorioInsertarI(ABC, Generic[T]):
    @abstractmethod
    def insert(self, modelo: T) -> None:
        pass

class RepositorioSelectI(ABC, Generic[T]):
    @abstractmethod
    def select(self, modelo: T) -> T:
        pass

class RepositorioSelectAllI(ABC, Generic[T]):
    @abstractmethod
    def select_all(self) -> list[T]:
        pass