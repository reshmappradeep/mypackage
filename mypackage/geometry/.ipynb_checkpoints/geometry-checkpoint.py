class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: "Point", p2: "Point") -> None:
        self.p1 = p1
        self.p2 = p2


    def length(self) -> float:
        return ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5

from ..utils import distance