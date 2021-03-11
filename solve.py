from reader import *
from writer import *
from random import randint

def main():
    filenames = ['b']

    for f in filenames:
        bestScore = 0
        for _ in range(100000):
            m = Map(f'{f}.in')
            l = len(m.antenne)

            used_pos = set()

            a = m.width-1
            b = m.heigth-1

            for i,ant in enumerate(m.antenne):
                p = (randint(0,a), randint(0,b))
                while p in used_pos:
                    p = (randint(0,a), randint(0,b))
                used_pos.add(p)
                m.setAntennaXY(i, p[0], p[1])

            score = m.tscore()
            if score > bestScore:
                bestScore = score
                writesol(f'{f}.out', m)
                m.save('mappa'+f+'.txt')
                print('New best score: ', bestScore)




if __name__ == '__main__':
	main()
