from reader import *
from writer import *
from random import randint

def main():
    filenames = ['a', 'b', 'c', 'd', 'e','f']

    for f in filenames:
        print(f'doing {f}')
        m = Map(f'{f}.in')
        buildingsSorted = sorted(m.buildings, key = lambda x: x.sweight,reverse=True)
        antenneSorted = sorted(m.antenne, key = lambda x: x.speed, reverse=True)

        for i,ant in enumerate(antenneSorted):
            #print(f'{i*100/m.m}% completato')
            m.setAntennaXY(i, buildingsSorted[i].x, buildingsSorted[i].y)

        writesol(f'{f}.out', m)
        m.save('mappa' + f + '.txt')

if __name__ == '__main__':
	main()
