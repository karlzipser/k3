from k3 import *

r = [
		#[r'^(([\s|\w|_|\d|\.|\-|`|~|\!|@|#|\$|%|\^|&|*|\(|\)|\[|\]|\{|\}]+/)+)$',
		#['this is a/test/path!/',]],

		[
			r'^\s*(\d+)\s*(\w*)$',
				[
					'127',
					' 127 ',
					'127o',
					'127oab',
					'127 o',
					'127 oab'
				],
		],
]


for q in r:
	_re = q[0]
	clp('\n')
	clp('r'+qtd(_re),'`--r')
	for _s in q[1]:
		clp('   ',qtd(_s))
		m = re.match(_re,_s)
		if m:
			clp('   ',m.groups())
		else:
			print(False)
		print('\n')
		time.sleep(1)




#EOF
