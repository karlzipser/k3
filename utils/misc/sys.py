
from k3.utils.misc.printing import *


def os_system(*args,e=0,r=0,a=1):
    s = d2s(*args)
    if(e):
        clp(s,'`---')
    if a:
        os.system(s)
    if r:
        raw_enter()




def unix(command_line_str, print_stdout=False, print_stderr=False,print_cmd=False):

    command_line_str = command_line_str.replace('~',home_path)

    p = subprocess.Popen(command_line_str.split(), stdout=subprocess.PIPE)

    stdout,stderr = p.communicate()

    if type(stdout) == bytes:
        stdout = stdout.decode('utf8')

    if type(stderr) == bytes:
        stderr = stderr.decode('utf8')

    if print_cmd:
        clp('print_cmd:','`--u',command_line_str,'\n',)

    if print_stdout:
        clp('print_stdout:','`--u',stdout,'\n',)

    if print_stderr:

        clp('print_stderr:','`--u',stderr,'\n',)

    return stdout.split('\n')





def gpu_stats(num=500):

    clp('Getting GPU stats...','`rwb')
    Pa = Percent(title='',prefix='',end_prefix=None)#Progress_animator(num,update_Hz=10,message='')
    GPUs_avg = {}
    for i in range(num):
        GPUs_avg[i] = {}

    nvidia_smi_str_lst = unix('nvidia-smi')
    GPUs = {}

    for i in range(num):
        ctr = 0
        
        for n in nvidia_smi_str_lst:
            if 'C' in n and 'W' in n and '%' in n:
                if ctr not in GPUs.keys():
                            GPUs[ctr] = {}
                GPUs[ctr]['line'] = n
                a = n.split('%')
                if 'fan' not in GPUs[ctr]:
                    #cm(0)
                    GPUs[ctr]['fan'] = 0
                if 'util' not in GPUs[ctr]:
                    GPUs[ctr]['util'] = 0
                    #cm(0)
                GPUs[ctr]['fan'] += int(a[0].split(' ')[-1])
                GPUs[ctr]['util'] += int(a[1].split(' ')[-1])
                ctr += 1
                #print i,ctr
        Pa['show'](i,num)
        time.sleep(0.01)
    Pa['show'](i,num)

    GPUs['most_free'] = 0
    GPUs['most_free_util'] = 100
    for i in range(ctr):
        GPUs[i]['fan'] /= 1.0*num
        GPUs[i]['util'] /= 1.0*num
        if GPUs[i]['util'] < GPUs['most_free_util']:
            GPUs['most_free_util'] = GPUs[i]['util']
            GPUs['most_free'] = i
    zprint(GPUs)
    return GPUs




def Bsave(D,name,bucket=opjh('bucket'),max_older=3):
    olds = sggo(bucket,d2n(name,'.*'))
    temp = opj(bucket,d2n('----',name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    os_system('mkdir -p',bucket)
    so(D,temp)
    final = opj(bucket,d2n(name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    os_system('mv',temp,final)
    if len(sggo(opj(bucket,d2n('----',name,'.*')))) > 0:
        os_system('rm',opj(bucket,d2n('----',name,'.*')))
    for i in range(max(0,(len(olds)-max_older+1))):
        os_system('rm',olds[i],e=0)


_loadDic = {'last_mtime':0}
def Bload(name,bucket=opjh('bucket')):
    fs = sggo(bucket,name+'*')
    M = {}
    for f in fs:
        M[os.path.getmtime(f)] = f
    new_f = M[sorted(kys(M))[-1]]
    mtime = os.path.getmtime(new_f)
    if mtime <= _loadDic['last_mtime']:
        return None
    else:
        _loadDic['last_mtime'] = mtime
        return lo(new_f)


def find(src,pattern,e=0,r=0,a=1):
    tempfile = opjD(d2p('find','temp',random_with_N_digits(9),'txt'))
    os_system('find',src,'-name',qtd(pattern),">",tempfile,e=e,r=r,a=a)
    find_list = txt_file_to_list_of_strings(tempfile)
    os_system("rm",tempfile)
    return find_list

    
if __name__ == '__main__':
    
    s = "os_system('ls',e=1,r=0)"

    clear_screen()
    clp('Examples from',__file__,'`--r')
    
    clp('Example:',s,'`--r')

    exec(s)

    s = "o = unix('ls',True,True,True)"

    print('\n')
    clp('Example:',s,'`--r')

    exec(s)
    kprint(o,s+' # kprint of output',)

#EOF

