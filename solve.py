from reader import *
from writer import *
from random import randint

def main():
	filenames = ['a', 'b', 'c', 'd', 'e', 'f']

	for f in filenames:
		m = Map(f'{f}.in')

		a = m.width-1
		b = m.heigth-1

		for i,ant in enumerate(m.antenne):
			m.setAntennaXY(i, randint(0,a), randint(0,b))

		writesol(f'{f}.out', m)




if __name__ == '__main__':
	main()