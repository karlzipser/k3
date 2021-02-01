

t = 30
os_system('say',qtd(d2s(t,'seconds')))
os_system('say "ready set go!"')
time.sleep(t)
os_system('say "stop!"')



def print_list_segment(
    list_of_paths,
    blanked_list_of_paths,
    i,
    minus=0,
    plus=1,
):
    import numpy as np
    if i - minus < 0:
        start = 0
    else:
        start = i - minus

    if i + plus > len(list_of_paths):
        stop = len(list_of_paths)
    else:
        stop = i + plus

    clear_screen()

    for j in range(start,stop):

        if j == i:
            fmt = '`--rb'
        else:
            fmt = '`--d'

        if j == start:
            s = list_of_paths[j]
        else:
            s = blanked_list_of_paths[j]

        if j == 0:
            l = 0
        else:
            l = int(np.log10(j))
            l = min(5,l)
        
        offset = ' ' * (5-l)
        clp(d2n(offset,j,') ',s),fmt)
        #print(list_of_paths[j])
        #print(blanked_list_of_paths[j])



def get_lists_of_paths(fs):
    fs = sorted(fs,key=natural_keys)
    #from natsort import natsorted
    #fs = natsorted(fs)
    lfs = []
    ls = []
    for f in fs:
        f = f.replace(' ','@')
        f = re.sub('^.*Users\/'+username+'\/','',f)
        lfs.append(f.split('/'))
        ls.append('/'+f)
    bs = [ls[0]]
    for i in range(1,len(lfs)):
        a = lfs[i-1]
        b = lfs[i]
        d = []
        no_difference = True
        for j in rlen(b):
            if j < len(a) and no_difference and b[j] == a[j]:
                c = ' '*(len(b[j])+1)
            else:
                c = '/'+b[j]
                no_difference = False
            d.append(c)
        bs.append(''.join(d))

    list_of_paths = ls
    blanked_list_of_paths = bs

    for i in range(len(blanked_list_of_paths)-1,0,-1):
        f = blanked_list_of_paths[i]
        g = blanked_list_of_paths[i-1]
        k = 0
        h = list(g)
        st = ['/','|']
        first = True
        for k in rlen(g):
            if not first:
                st = ['|']
            if len(f) > k and f[k] in st:
                if f[k] == '/':
                    first = False
                if h[k] == ' ':
                    h[k] = '|'
        blanked_list_of_paths[i-1] = ''.join(h).replace('@',' ')

    for i in rlen(list_of_paths):
        list_of_paths[i] = list_of_paths[i].replace('@',' ')

    return list_of_paths, blanked_list_of_paths



fs = find_files(
    start='Stowed/2019',
    patterns=['*.jpeg','*.jpg','*.png','*.JPG','*.JPEG','*.JPG','*.PNG'],
    ignore=[],
    recursive=True
)




list_of_paths, blanked_list_of_paths = get_lists_of_paths(fs)



for i in range(len(blanked_list_of_paths)):
    q = get_terminal_size()[0]
    minus = q - 6
    plus = 4
    print_list_segment(list_of_paths,blanked_list_of_paths,i,minus,plus)
    #time.sleep(.1)#;
    raw_enter() 


glob.glob('mobile-documents/**/*∆ƒ*',recursive=True) 

#EOF
