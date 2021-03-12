from reader import *
from writer import *
from random import randint

def main():
    filenames = ['b']

    for f in filenames:
        bestScore = 0
        m = Map(f'{f}.in')
        final_used = set()
        final_antenne = []
        cluster = 50
        for k in range(len(m.antenne) // cluster + 1):
            best_used = set()
            best_antenne = []
            for j in range(50):
                tmp_used = set()
                tmp_antenne = []

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
                    tmp_antenne.append([k*cluster + i, p[0], p[1]])

                score = m.tscore()
                if score > bestScore:
                    best_used = tmp_used
                    best_antenne = tmp_antenne
                    bestScore = score
                    #writesol(f'{f}.out', m)
                    #m.save('mappa'+f+'.txt')
                    print('New best score: ', bestScore, ' iterazione numero ', j, 'cluster numero ', k)
            
            final_used = final_used.union(best_used)
            final_antenne = final_antenne + best_antenne
            for a in best_antenne:
                m.setAntennaXY(a[0], a[1], a[2])

        print(len(final_antenne))
        used = {}
        for t in final_antenne:
            m.setAntennaXY(a[0], a[1], a[2])

            _id = (t[1], t[2])
            if _id in used.keys():
                used[_id].append(t[0])
                print(f'Posizione {_id} usata da {used[_id]}')
            else:
                used[_id] = [t[0]]

        writesol(f'{f}.out', m)
        m.save('mappa'+f+'.txt')

if __name__ == '__main__':
	main()
