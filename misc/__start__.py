print('Running '+'/'.join(__file__.split('/')[-3:]))

from k3 import *

try:
	D = loD('D',noisy=True)
except:
	D = {}

def zexit():

	soD(D,'D',noisy=True)

	exit()

#EOF
