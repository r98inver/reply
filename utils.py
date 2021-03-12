def dupCheck(f):
	fh = open(f'{f}.out')
	txt = fh.read()
	fh.close()

	txt = txt.split('\n')
	txt = txt[1:-1]
	txt = list(map(lambda x: x.split(' ' ), txt))

	used = {}
	for t in txt:
		_id = (t[1], t[2])
		if _id in used.keys():
			used[_id].append(t[0])
			print(f'Posizione {_id} usata da {used[_id]}')
		else:
			used[_id] = [t[0]]

dupCheck('b')