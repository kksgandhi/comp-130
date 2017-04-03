class Shape:

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return " ".join(str(e) for e in self.points)

shep = Shape([1, 2])
print shep
