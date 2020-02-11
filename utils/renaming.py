from __future__ import print_function
from __future__ import division

from basic_imports import *

rnd = np.random.random
rndint = np.random.randint
rndn = np.random.randn
rndchoice = np.random.choice
na = np.array
hostname = socket.gethostname()
homepath = os.path.expanduser("~")
username = getpass.getuser()
try:
    imread = scipy.misc.imread
    imsave = scipy.misc.imsave
    imresize = scipy.misc.imresize
except:
    print("failed: imread = scipy.misc.imread, imsave = scipy.misc.imsave")
degrees = np.degrees
arange = np.arange
shape = np.shape
zeros = np.zeros
ones = np.ones
reshape = np.reshape
mod = np.mod
array = np.array

#EOF
