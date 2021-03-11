from reader import *
from writer import *
from random import randint

def main():
	filenames = ['a', 'b', 'c', 'd', 'e', 'f']

	for f in filenames:
		m = Map(f'{f}.in')
		l = len(m.antenne)

		used_pos = set()

		a = m.width-1
		b = m.heigth-1

		for i,ant in enumerate(m.antenne):
			print(f'{i*100/l}% completato')
			p = (randint(0,a), randint(0,b))
			while p in used_pos:
				p = (randint(0,a), randint(0,b))
			used_pos.add(p)
			m.setAntennaXY(i, p[0], p[1])

		writesol(f'{f}.out', m)




if __name__ == '__main__':
	main()