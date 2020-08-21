
from k3.utils.core.renaming import *

_which_python = sys.version.split(' ')[0]
if _which_python[0] == '3':
    raw_input = input
    using_python3 = True
else:
    using_python3 = False
del _which_python

os.environ['PYTHONUNBUFFERED'] = '1'

#EOF