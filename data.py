import threading
from dataclasses import dataclass


@dataclass
class TwoDimensions:
    x: int
    y: int


@dataclass
class RegionIdx(TwoDimensions):
    pass


@dataclass
class BlockIdx(TwoDimensions):
    pass


@dataclass
class BlockIx(TwoDimensions):
    pass


@dataclass
class ThreadIdx(TwoDimensions):
    name: str

    def get(self):
        return threading.Thread(name=self.name)


@dataclass
class RegionDim(TwoDimensions):
    pass

