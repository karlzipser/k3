
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



iCloud_bucket = opjh("Library/Mobile Documents/com~apple~CloudDocs/iCloud-bucket")
def Bsave(D,name,bucket=opjh('bucket'),max_older=3):
    olds = sggo(bucket,d2n(name,'.*'))
    temp = opj(bucket,d2n('----',name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    final = opj(bucket,d2n(name,'.',time.time(),'.',random_with_N_digits(9),'.pkl'))
    os_system('mkdir -p',bucket)
    so(temp,D,noisy=True)
    os_system('mv',qtd(temp),qtd(final))
    for f in sggo(opj(bucket,d2n('----',name,'.*'))):
        os_system('rm',qtd(f),e=1)
    for i in range(max(0,(len(olds)-max_older+1))):
        os_system('rm',qtd(olds[i]),e=0)


IGNORE_INT,IGNORE_FLOAT,IGNORE_STR = -99999,-9999.99,'-9999.99'
_Bload = {}
def Bload(name,Dst=None,bucket=opjh('bucket'),starttime=0,ignore_underscore=True):
    fs = sggo(bucket,name+'*')
    if len(fs) == 0:
        return None
    M = {}
    for f in fs:
        M[os.path.getmtime(f)] = f
    new_f = M[sorted(kys(M))[-1]]
    mtime = os.path.getmtime(new_f)
    if mtime < starttime:
        return None
    if name not in _Bload:
        _Bload[name] = {}
    elif mtime <= _Bload[name]['last_mtime']:
        return None
    _Bload[name]['last_mtime'] = mtime
    D = lo(new_f)
    if type(Dst) is dict and type(D) is dict:
        for k_ in kys(D):
            if k_[0] == '_' and ignore_underscore:
                continue
            #if D[k_] in [IGNORE_INT,IGNORE_FLOAT,IGNORE_STR]:
            #    continue
            if k_ not in Dst:
                cE("Bload:",k_,'not in',Dst)
            assert k_ in Dst
            Dst[k_] = D[k_]
            #cm('Dst[',k_,'] =',D[k_])
    return D


# find iCloud_Links  \( -name '*.JPG' -o -name "*.jpg" \) -print

def find(src,pattern,e=0,r=0,a=1):
    tempfile = opjD(d2p('find','temp',time.time(),random_with_N_digits(9),'txt'))
    os_system('find',src,'-name',qtd(pattern),">",tempfile,e=e,r=r,a=a)
    find_list = txt_file_to_list_of_strings(tempfile)
    find_list = sorted(find_list)
    os_system("rm",tempfile)
    return find_list

    
def should_I_start(_file_,dt=60,verbose=False):
    path = opjh('bucket/times',get_safe_name(_file_))
    os_system('mkdir -p',pname(path),e=0)
    if len(sggo(path)) > 0:
        mt = os.path.getmtime(path)
    else:
        mt = 0
    if verbose:
        print('time since',fname(_file_),'last touched =',dp(time.time() - mt))
    if time.time() - mt < dt:
        if verbose:
            print('not starting',fname(_file_))
        sys.exit()
    return path
    


def do_dialog(text,title):
    tempfile = get_temp_filename(path=opjb())
    os_system(
        "osascript -e 'Tell application \"System Events\" to display dialog",
        qtd(text),
        "with title \""+title+"\"' > " + tempfile
    )
    output = file_to_text(tempfile)
    os_system('rm',tempfile)
    return output



def memory():
    """
    Get node total memory and memory usage
    http://stackoverflow.com/questions/17718449/determine-free-ram-in-python
    """
    if using_osx():
        import psutil
        m = psutil.virtual_memory()
        return m.percent
    else:
        with open('/proc/meminfo', 'r') as mem:
            ret = {}
            tmp = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) == 'MemTotal:':
                    ret['total'] = int(sline[1])
                elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                    tmp += int(sline[1])
            ret['free'] = tmp
            ret['used'] = int(ret['total']) - int(ret['free'])
        return ret



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

