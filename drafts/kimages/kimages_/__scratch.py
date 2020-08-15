


if False: ##### KEEP!!!!
    q="Pictures/Photos Library.photoslibrary/Masters/2020"
    heics=get_list_of_files_recursively(q,'*.HEIC',FILES_ONLY=True,ignore_underscore=False)
    jpgs=get_list_of_files_recursively(q,'*.JPG',FILES_ONLY=True,ignore_underscore=False)
    js,hs = [],[]
    for j in jpgs:
        js.append(fnamene(j))
    for j in heics:
        hs.append(fnamene(j))
    n = 0
    for j in js:
        if j not in hs:
            n += 1
            cg(j,n,int(n/(1.0*len(js))*100),'%')
    raw_enter()
    n = 0
    for j in hs:
        if j not in js:
            n += 1
            cg(j,n,int(n/(1.0*len(js))*100),'%')


if False:
    class Cdat:
        def __init__(self,title=''):
            self._title=title
        def add(self, name, val):
            self.__dict__[name] = val
        def kprint(self):
            kprint(vars(self),title=self._title)

    G = Cdat('G')
    G.add('value_1', 'Just me.')
    G.add('value_2', 1)
    G.add('value_3', {'a':'Just me.',2:'adfadsf'})
    G.kprint()

p = "Pictures/Photos Library.photoslibrary/originals/0"
fs = get_list_of_files_recursively(q,'*.jpeg',FILES_ONLY=True,ignore_underscore=False)
T = {}
for f in fs:
    if f[0] == '/':
        f = f[1:]
    t = time_str(t=os.path.getmtime(f))
    T[f] = t
kprint(T)



#,a
p = "Pictures/Photos Library.photoslibrary/originals"

fs = get_list_of_files_recursively(p,'*.*',FILES_ONLY=True,ignore_underscore=False)
get_time = os.path.getmtime
F = {}
for f in fs:
    if f[0] == '/':
        f = f[1:]
    f = opj(p,f)
    ex = exname(f)
    t = get_time(f)
    if ex not in F:
        F[ex] = {}
    F[ex][f] = time_str(t=t)
kprint(F)

jpeg_names = []
for f in F['jpeg']:
    jpeg_names.append(fname(f))

#,

conversion_dir = opjh('Pictures/heic_to_jpeg')
existing = sggo(conversion_dir,'*.jpeg')
os_system('mkdir -p',conversion_dir)
i = 0
for f in F['heic']:
    skip = False
    for e in existing:
        if fnamene(f) in e:
            skip = True
    if skip:
        cm('skip',f,'because already converted to .jpeg')
        i += 1
        continue
    f = f.replace(' ','\ ')
    n = fnamene(f)+'.jpeg'
    if n in jpeg_names:
        cb(n,'in jpeg_names')
    elif len(sggo(conversion_dir,n)) > 0:
        cr(n,'already processed')
    else:
        cy(as_pct(i,len(F['heic'])))
        d = opj(conversion_dir,n).replace(' ','\ ')
        os_system('convert',f,d,e=1)
    i += 1
    #raw_enter()






#,b