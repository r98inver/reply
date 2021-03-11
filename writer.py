def writesol(outfile, M):
	# Prima riga numero di antenne
	# id x y

	ant = Map.antenne
	out = ''

	out += len(ant)+'\n'

	for i,a in enumerate(ant):
		out += f'{i} {a.x} {a.y}'

	with open(outfile, 'w') as o:
		o.write(out)

	