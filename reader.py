class Building(object):

    def __init__(self, row):
        self.x, self.y, self.lweight, self.sweight = list(map(int, row.split(' ')))

class Antenna(object):

    def __init__(self, row):
        self.range, self.speed = list(map(int, row.split(' ')))

class Map(object):

    def __init__(self, filename):
        f = open(filename, 'r')
        text = f.read()
        righe = text.split('\n')
        self.width, self.heigth = list(map(int, righe[0].split(' ')))
        self.n, self.m, self.reward = list(map(int,righe[1].split(' ')))
        self.buildings = []
        for i in range(self.n):
            self.buildings.append(Building(righe[2+i]))
        self.antenne = []
        for i in range(self.m):
            self.antenne.append(Antenna(righe[2+self.n+i]))
