def writesol(outfile, M):
	# Prima riga numero di antenne
	# id x y

	ant = M.antenne
	out = ''

	out += f'{len(ant)}\n'

	for i,a in enumerate(ant):
		out += f'{i} {a.x} {a.y}\n'

	with open(outfile, 'w') as o:
		o.write(out)

	