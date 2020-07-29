#,a
from k3.utils3 import *

def a(**p):

	dargs({
		'rest':'well',
		'1':'a',
		'2':[1,2,3],
		'3':'c',
		},
		p,
		required=['q'])

	clp('---',fl())

	kprint(p,title='p modified')
	
	clp('---',fl())

if __name__ == '__main__':
	Arguments = get_Arguments()
	kprint(Arguments,title='p input')
	a(**Arguments)

#,b

