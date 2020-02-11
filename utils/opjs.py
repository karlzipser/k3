from __future__ import print_function
from __future__ import division

from have_using import *


def opj(*args):
    if len(args) == 0:
        args = ['']
    str_args = []
    for a in args:
        str_args.append(str(a))
    return os.path.join(*str_args)
def opjh(*args):
    return opj(os.path.expanduser("~"),opj(*args))
def opjD(*args):
    return opjh('Desktop',opj(*args))
def opjk(*args):
    return opjh('k3',opj(*args))
def opjm(*args):
    if not using_osx():
        media_path = opj('/media',username)
        return opj(media_path,opj(*args))
    else:
        media_path = '/Volumes'
        return opj(media_path,opj(*args))

#EOF
