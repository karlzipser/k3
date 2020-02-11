from __future__ import print_function
from __future__ import division

from renaming import *

def nvidia_smi_continuous(t=0.1):
    while True:                                     
        os.system('nvidia-smi',print_stdout=True)
        time.sleep(t)


#EOF

