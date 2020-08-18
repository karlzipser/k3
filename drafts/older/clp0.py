#,a
from k3.utils3 import *

def a():

	data = sys.argv[1:]
	print data
	clp(*data[0].split(','))

if __name__ == '__main__':

	a()
#,b

