
from k3 import *

def remove_empty(l):
	m = []
	for a in l:
		if a != '':
			m.append(a)
	return m

def space(s):
	a = s.split(' ')
	return remove_empty(a)


def args_to_dict(s):
	#print(s)
	m = space(s)
	n = []
	keyword_found = False
	for a in m:
		if not str_is_float(a):
			if a[0] == '-':
				n.append('KEYWORD='+a)
				continue
		if not keyword_found:
			keyword_found = True
			n.insert(0,'KEYWORD=--positional_args')
		n.append(a)
	o = ' '.join(n)
	print(o)
	q = o.split('KEYWORD=')
	print(q)
	r = remove_empty(q)
	#print(r)
	#EOF
	U = {}
	print(r)
	for a in r:
		b = space(a)
		#cg(b)
		c = b[0]
		if len(c) == 2:
			assert c[0] == '-'
			assert c[1].isalpha()
		elif len(c) > 3:
			assert c[0] == '-'
			assert c[1] == '-'
			assert c[2].isalpha()
			for i in range(3,len(c)):
				assert c[i].isalpha() or c[i].isnumeric() or c[i] in ['_','.',',']
		else:
			assert False

		d = b[0].replace('-','')
		if len(b) == 1:
			U[d] = True
		elif len(b) == 2:
			if str_is_int(b[1]):
				U[d] = int(b[1])
			elif str_is_float(b[1]):
				U[d] = float(b[1])
			else:
				U[d] = b[1]
		else:
			U[d] = b[1:]
	if U['positional_args'] == True:
		del U['positional_args']

	return U


s = 'abc def --a1 1as --rnd 123 -a -b 32.1 --Cfadf -f -3 ,,, , --f1_ 3 -x 1 2 3 -z a'
U = args_to_dict(s)
zprint(U)




