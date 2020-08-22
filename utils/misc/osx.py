
from k3.utils.misc.sys import *

    



def stowe_Desktop(suffix=''):
    if len(suffix) > 0:
        suffix = '__' + suffix
    dst = opjh('Desktops_older','Desktop_'+time_str()+suffix)
    print(dst)
    unix('mkdir -p ' + dst)
    #_,l = dir_as_dic_and_list(opjD(''))
    l = sggo(opjD('*'))
    for m in l:
        shutil.move(m,dst)


def restore_Desktop(src):
    l = sggo(opjD('*'))
    if len(l) > 0:
        print('**** Cannot restore Desktop because Desktop is not empty.')
        return False
    l = sggo(opj(src,'*'))
    for m in l:
        shutil.move(m,opjD())



#EOF
