from k3.utils.core.files.files import *

Arguments = args_to_dict('--one 1111 --two 2222 --three 3333')


def main(**A):
    print_dic_simple(A)
    soD('temp',A)
    B = loD('temp')
    os.system('rm ' + opjD('temp.pkl'))
    print_dic_simple(B)
    
    
def save_obj(obj, name,noisy=True,show_time=False,use_real_path=False):
    assert_disk_locations([pname(name)])
    name = name.replace('.pkl','')
    if use_real_path:
        name = os.path.realpath(name)
    with open(name + '.pkl', 'wb') as f:
        if use_real_path:
            f = os.path.realpath(f)
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    if noisy:
        timer = Timer()
        a = d2s('. . . saved','`',name+'.pkl','`--rb')
        if show_time:
            b = d2s('`','in',dp(timer.time()),'seconds.\r')
        else:
            b=''
        pd2s(a,b)


def load_obj(name,noisy=True,time=False,use_real_path=False):
    assert_disk_locations([pname(name)])
    if noisy:
        timer = Timer()
        #clp('Loading','`',name,'`--rb','. . .\r'),
        pd2s('Loading',name,'. . .\r'),
    name = name.replace('.pkl','')
    name = name + '.pkl'
    if use_real_path:
        name = os.path.realpath(name)
    assert_disk_locations(name)
    with open(name, 'rb') as f:
        o = pickle.load(f)
        if noisy:
            pd2s(d2s('. . . loaded in',dp(timer.time()),'seconds.\r')),
        return o
        
lo = load_obj

def loD(name,noisy=True,use_real_path=False):
    if use_real_path:
        name = os.path.realpath(name)
    return load_obj(opjD(name),noisy)

def so(arg1,arg2,noisy=True):
    if True:#try:
        if type(arg1) == str and type(arg2) != str:
            save_obj(arg2,arg1,noisy)
            return
        if type(arg2) == str and type(arg1) != str:
            save_obj(arg1,arg2,noisy)
            return
        if type(arg2) == str and type(arg1) == str:
            pd2s('def so(arg1,arg2): both args cannot be strings')
        assert(False)
    else:#except:
        print("exec(EXCEPT_STR)")

def soD(arg1,arg2,noisy=True):
    if True:#try:
        if type(arg1) == str and type(arg2) != str:
            save_obj(arg2,opjD(arg1),noisy)
            return
        if type(arg2) == str and type(arg1) != str:
            save_obj(arg1,opjD(arg2),noisy)
            return
        if type(arg2) == str and type(arg1) == str:
            pd2s('def so(arg1,arg2): both args cannot be strings')
        assert(False)
    else:#except:
        print("exec(EXCEPT_STR)")


if __name__ == '__main__':
    Arguments = get_Arguments(Arguments)
    eg(__file__)
    main()

#EOF
