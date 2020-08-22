#!/usr/bin/env python
from k3.utils import *

def backup_folder(
    src=opjh('k3')+'/',
    dst=opjh('_k3_older','k3_'+time_str())+'/'
    ):
    """
    Make a time marked backup, with default as k3.
    """
    os.system('mkdir -p ' + dst)
    os.system(d2s("rsync -ravL --exclude '*.pyc' --exclude '*.pkl'", src, dst))

backup_folder()

#EOF