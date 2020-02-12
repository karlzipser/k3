from __future__ import print_function
from __future__ import division

from basics import *

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

SCRATCH = False

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
    
#EOF
