
from k3.utils.misc.printing import *

def by_keylist(D,keylist):
	for i in rlen(keylist):
		k = keylist[i]
		if k in D:
			D = D[k]
		else:
			pd2s(k,'is not in',D)
			while len(keylist) > i:
				keylist.pop()
	return D


def Navigate_Dictionary(D,ignore_keys=['.meta']):
	"""
	Does (should) not modify state of dict D.
	"""
	
	keylist = []

	def navigate():

		message = None

		while True:

			clear_screen()

			if len(keylist) > 0:
				t = keylist[-1]
			else:
				t = 'D'
			kprint(by_keylist(D,keylist),ignore_keys=ignore_keys)
			print('')
			clp('choices','`--u')

			current = by_keylist(D,keylist)
			if type(current) is not dict:
				up()
				return current

			if message is not None:
				print(message)
			message = None

			ks = list(current.keys())
			for ik in ignore_keys:
				if ik in ks:
					pd2s('ignoring',ik)
					ks.remove(ik)

			int_choices = list(range(1,len(ks)+1))
			for i in int_choices:
				pd2s(i,')',ks[i-1])

			q = raw_input('> ')

			if q == 'q':
				return None

			elif q == '0':
				message = up()

			elif q == 'e':
				return current

			elif str_is_int(q):

				#print(int(q),int_choices)
				if int(q) not in int_choices:
					message = d2s('***',q,'not valid number choice')
					continue

				q = ks[int(q)-1]

				down(q)

			else:
				message = d2s('***',q,'not valid choice')

	def down(k):
		keylist.append(k)
		return by_keylist(D,keylist)
	
	def up():
		if len(keylist) > 0:
			keylist.pop()
			return 'went up'
		else:
			return 'already at top'
		
	
	return namedtuple('_', 'navigate up down keylist')(navigate,up,down,keylist)


if __name__ == '__main__':

	print('\nExample of using Navigate_Dictionary')
	
	Q = {
	    '1':{
	        '2':{
	            '.meta':[5,6],
	            'a':1,
	        '7':{'xx':['a','v','r',[1,2,3]]},
	        '8':'eight',
	        }
	    },
	    'qqq':'zzz',
	}

	N = Navigate_Dictionary(Q)

	while True:
		print('')
		q = raw_input(d2s(qtd('n'),'to navigate,',qtd('e'),'to exit navigation',qtd('q'),'to quit, or anything else > '))
		if q == 'q':
			break
		elif q == 'n':
			result = N.navigate()
			pd2s('\nWe got',result,'out of navigation.')
		else:
			print('\nDoing something else...')


#EOF
