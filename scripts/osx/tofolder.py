
#,tf.a
"""
python3 k3/scripts/osx/tofolder.py\

"""
#,tf.b


from k3.utils import *

A = get_Arguments(
    {
        'name':'',
        'del':False,
    },
    file=__file__,
    r=False,
)


exec(A_to_vars_exec_str)

fs = select_files(opjD())

if del_:
    for f in fs:
        os_system('mv',qtd(f),opjh(".Trash"),a=1,e=1)

else:    
    if A['name'] == '':
        A['name'] = input('Enter name for new folder to put files in => ')

    A['name'] = d2p(get_safe_name(A['name']),time_str('FileSafe'))


    dst = opjD(A['name'])
    os_system('mkdir -p',dst)

    for f in fs:
        os_system('mv',qtd(f),qtd(dst),a=1,e=1)


#EOF
