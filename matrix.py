from random import random


class Matrix(list):
    def __init__(self):
        super().__init__()
        self._order = None
        self._matrix = None

    def _create(self, n: int):
        self._order = n
        self._matrix = [[random() for _ in range(n)] for _ in range(n)]

    def get(self, n: int) -> list[list[float]]:
        self._create(n)
        return self._matrix

    @property
    def x(self):
        return self._order

    @property
    def y(self):
        return self._order
