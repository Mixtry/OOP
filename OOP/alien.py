class Alien:
    def __init__(self, name:str, vol, fill):
        self.name = name
        self.vol = vol
        self.fill = fill

    def __repr__(self):
        return f"Alien('{self.name}', {self.vol}, {self.fill})"

    def __le__(self, other):
        return (self.vol * self.fill, len(self.name)) <= (other.vol * other.fill, len(other.name))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.vol * self.fill == other.vol * other.fill:
            if len(self.name) == len(other.name):
                if self.name < other.name:
                    return self.name < other.name
                return self.name > other.name
            return len(self.name) < len(other.name)
        return self.vol * self.fill < other.vol * other.fill

    def __gt__(self, other):
        if self.vol * self.fill == other.vol * other.fill:
            if len(self.name) == len(other.name):
                return self.name > other.name
            return len(self.name) > len(other.name)
        return self.vol * self.fill > other.vol * other.fill


    def __add__(self, other):
        name = '-'.join(sorted([self.name, other.name]))
        vol = (self.vol + other.vol) // 2
        fill = min(self.fill, other.fill)
        return Alien(name, vol, fill)

    def __isub__(self, number):
        self.vol = max(self.vol - number, 0)
        return self

    def __mul__(self, number):
        return [Alien(f"{self.name}-{i+1}", self.vol // number, self.fill // number) for i in range(number)]

    def __call__(self, number):
        return (self.vol - self.fill) * len(self.name) // number

    def __eq__(self, other):
        return self.name == other.name and self.vol == other.vol and self.fill == other.fill

    def __ge__(self, other):
        if self.vol * self.fill == other.vol * other.fill:
            if len(self.name) == len(other.name):
                return self.name >= other.name
            return len(self.name) >= len(other.name)
        return self.vol * self.fill >= other.vol * other.fill

    def __str__(self):
        return f"Wheel Alien {self.name} with {self.vol} volume and filled up {self.fill}."

    def fill_up(self, number: int):
        return max(self.fill + number, 0)


al = Alien("man", 200, 148)
al1 = Alien("spider", 800, 201)
print(al <= al1, al != al1, al > al1)
print(al, al1, sep="\n")
print()
al.fill_up(-203)
res = al1 * 3
print(al, al1, res,sep="\n")
print(res[0](7))