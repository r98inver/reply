from reader import *
from writer import *
from random import randint

def main():
    filenames = ['b']

    for f in filenames:
        bestScore = 0
        m = Map(f'{f}.in')
        final_used = set()
        cluster = 200
        for k in range(len(m.antenne) // cluster + 1):
            best_used = set()
            for j in range(10):
                tmp_used = set()
                
                a = m.width-1
                b = m.heigth-1

                if (k+1)*cluster >= len(m.antenne):
                    b = len(m.antenne)
                else:
                    b = (k+1)*cluster
                for i,ant in enumerate(m.antenne[k*cluster:b]):
                    p = (randint(0,a), randint(0,b))
                    while p in tmp_used or p in final_used:
                        p = (randint(0,a), randint(0,b))
                    tmp_used.add(p)
                    m.setAntennaXY(k*cluster + i, p[0], p[1])

                score = m.tscore()
                if score > bestScore:
                    best_used = tmp_used
                    bestScore = score
                    writesol(f'{f}.out', m)
                    m.save('mappa'+f+'.txt')
                    print('New best score: ', bestScore, ' iterazione numero ', j, 'cluster numero ', k)
            final_used = final_used || best_used

if __name__ == '__main__':
	main()
