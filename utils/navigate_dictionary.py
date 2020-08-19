#,a

from k3.utils3 import *


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


def Navigate_Dictionary(D):
	
	keylist = []

	def navigate():

		message = None

		while True:

			clear_screen()

			if len(keylist) > 0:
				t = keylist[-1]
			else:
				t = 'D'
			kprint(by_keylist(D,keylist))#,t)
			print('')
			clp('choices','`--u')

			current = by_keylist(D,keylist)
			if type(current) is not dict:
				#cr(current)
				up()
				return current

			if message is not None:
				print(message)
			message = None

			ks = list(current.keys())
			int_choices = list(range(1,len(ks)+1))
			for i in int_choices:
				pd2s(i,')',ks[i-1])

			q = raw_input('> ')

			if q == 'q':
				return None

			elif q == '0':
				message = up()

			elif q == 'r':
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
		
	
	return namedtuple('_', 'navigate up down')(navigate,up,down)


if __name__ == '__main__':

	print('\nExample of using Navigate_Dictionary')
	
	Q = {
	    '1':{
	        '2':{
	            '3':[5,6],
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
		q = raw_input('n to navigate, q to quit, or anything else > ')
		if q == 'q':
			break
		elif q == 'n':
			result = N.navigate()
			pd2s('\nWe got',result,'out of navigation.')
		else:
			print('\nDoing something else...')
#,b

#EOF
