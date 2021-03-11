from reader import *
from writer import *
from random import randint
from multiprocessing import Pool


def main():
	filenames = ['a']

	for f in filenames:
		m = Map(f'{f}.in')
		l = len(m.antenne)

		global parall
		def parall(x):
			m.setAntennaXY(x[0], x[1], x[2])

		a = m.width-1
		b = m.heigth-1

		used_pos = set()
		for i in range(l):
			p = (randint(0,a), randint(0,b))
			while p in used_pos:
				p = (randint(0,a), randint(0,b))
			used_pos.add(p)

		ls = list(used_pos)
		ls1 = [(i, j[0], j[1]) for i,j in enumerate(ls)]
		
		pool = Pool()
	    foo[1] = pool.map(parall, ls1)
	    pool.close()
	    pool.join()

		writesol(f'{f}.out', m)
	

		


if __name__ == '__main__':
	main()