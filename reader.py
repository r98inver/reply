import math

class Building(object):

    def __init__(self, row):
        self.x, self.y, self.lweight, self.sweight = list(map(int, row.split(' ')))
        self.connectedAntenne = []

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

    def setAntennaXY(self, id, x, y):
        antenna = self.antenne[id]
        antenna.x = x
        antenna.y = y
        for building in self.buildings:
            if self.dist(antenna, building) <= antenna.range:
                building.connectedAntenne.append(antenna)

    def dist(self, antenna, building):
        return abs(antenna.x - building.x) + abs(antenna.y - building.y)

    def score(self, antenna, building):
        return building.sweight * antenna.speed - self.dist(antenna, building) * building.lweight

    def tscore(self):
        reward = True
        sum = 0
        for building in self.buildings:
            maxScore = 0
            if len(building.connectedAntenne) == 0:
                reward = False
            for antenna in building.connectedAntenne:
                scor = self.score(antenna, building)
                if scor > maxScore:
                    maxScore = scor
            sum += maxScore
        if reward:
            sum += self.reward
        return sum
