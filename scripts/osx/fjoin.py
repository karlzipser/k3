
#,fj.a
"""
python3 k3/scripts/osx/fjoin.py\

"""
#,fj.b


from k3.utils import *

A = get_Arguments(
    {
    	'paths':[],
        'new':'',
        'name':'',
    },
    file=__file__,
    r=False,
)

A['name'] = get_safe_name(A['name'])
exec(A_to_vars_exec_str)

#image_extensions = ['jpg','jpeg','png']

if len(paths_) == 0:
    paths_ = select_folders(opjh())
if new_ == '':
    if name_ == '':
        name_ = 'new'
    new_ = opjD(d2p(name_,time_str('FileSafe')))
#print(new_)
#print(paths_)

fs = []
for p in paths_:
    fs += sggo(p,'*')

#print(fs)

fs2 = []
for f in fs:
    #print(f)
    if os.path.isfile(f):
        #print('*')
        fs2.append(f)

os_system("mkdir -p",new_,a=1,e=1)
ctr = 0
for f in fs2:
    #print(ctr,f)
    #ctr += 1
    os_system("cp",f,opj(new_,fname(f)),a=1,e=1)

#EOF
