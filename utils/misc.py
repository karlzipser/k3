from __future__ import print_function
from __future__ import division

from renaming import *

def nvidia_smi_continuous(t=0.1):
    while True:                                     
        os.system('nvidia-smi',print_stdout=True)
        time.sleep(t)





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

