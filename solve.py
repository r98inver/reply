from reader import *
from writer import *
from random import randint

def main():
    filenames = ['b']

    for f in filenames:
        bestScore = 0
        m = Map(f'{f}.in')
        Old_used_pos = set()
        cluster = 100
        for k in range(len(m.antenne) // cluster + 1):
            for j in range(50):
                used_pos = Old_used_pos.copy()
                a = m.width-1
                b = m.heigth-1

                if (k+1)*cluster >= len(m.antenne):
                    b = len(m.antenne)
                else:
                    b = (k+1)*cluster
                for i,ant in enumerate(m.antenne[k*cluster:b]):
                    p = (randint(0,a), randint(0,b))
                    while p in used_pos:
                        p = (randint(0,a), randint(0,b))
                    used_pos.add(p)
                    m.setAntennaXY(i, p[0], p[1])

                score = m.tscore()
                if score > bestScore:
                    Old_used_pos = used_pos
                    bestScore = score
                    writesol(f'{f}.out', m)
                    m.save('mappa'+f+'.txt')
                    print('New best score: ', bestScore, ' iterazione numero ', j, 'cluster numero ', k)


if __name__ == '__main__':
	main()
