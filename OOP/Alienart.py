class AlienArtifact:
    def __init__(self, length, width, height, color):
        self.length = length
        self.width = width
        self.height = height
        self.color = color

    def __lt__(self, other):
        return self.vol() < other.vol() or (self.vol() == other.vol() and len(self.color) < len(other.color)) or (self.vol() == other.vol() and len(self.color) == len(other.color) and self.color < other.color)

    def __le__(self, other):
        return self.vol() <= other.vol() or (self.vol() == other.vol() and len(self.color) < len(other.color)) or (self.vol() == other.vol() and len(self.color) == len(other.color) and self.color <= other.color)

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width and self.height == other.height and self.color == other.color

    def __add__(self, other):
        length = (self.length + other.length) // 2
        width = (self.width + other.width) // 2
        height = (self.height + other.height) // 2
        color = min(self.color, other.color)
        return AlienArtifact(length, width, height, color)

    def __iadd__(self, other):
        self.length += other // 3
        self.width += other // 3
        self.height += other // 3
        return self

    def __mul__(self, other):
        length = max(self.length // other, 1)
        width = self.width
        height = self.height * other
        color = self.color
        return [AlienArtifact(length, width, height, color) for _ in range(other)]

    def __call__(self):
        return self.vol()

    def change_color(self, color):
        self.color = color

    def __str__(self):
        return f"This is an alien artifact with {self.color} color and {self.vol()} volume."

    def __repr__(self):
        return f"AlienArtifact({self.length}, {self.width}, {self.height}, '{self.color}')"

    def vol(self):
        return self.length * self.width * self.height


aa = AlienArtifact(5, 4, 3, "cloudy")
aa1 = AlienArtifact(5, 3, 4, "gloomy")
print(aa < aa1, aa == aa1, aa >= aa1)
print(aa, aa1, sep="n")
print()
aa.change_color("black")
aa1 += 17
aa2 = aa + aa1
print(aa, aa1, aa2, sep="n")