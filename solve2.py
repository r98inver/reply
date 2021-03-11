from reader import *
from writer import *
from random import randint

def main():
    filenames = ['c']

    for f in filenames:
        m = Map(f'{f}.in')
        buildingsSorted = sorted(m.buildings, key = lambda x: x.sweight)
        antenneSorted = sorted(m.antenne, key = lambda x: x.speed)

        for i,ant in enumerate(antenneSorted):
            print(f'{i*100/m.m}% completato')
            m.setAntennaXY(i, buildingsSorted[i].x, buildingsSorted[i].y)

        writesol(f'{f}.out', m)
        m.save('mappa' + f + '.txt')

if __name__ == '__main__':
	main()
