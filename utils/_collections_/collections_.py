from k3.utils.core import *

REQUIRED = '__REQUIRED__'
#,a

if False:
    def kys(D):
        return list(sorted(D.keys()))
    
    
    def set_Defaults(Defaults,Dst):
        for k in Dst.keys():
            if k not in Defaults.keys():
                cr("**** Warning, argument '"+k+"' not in expected Dst:\n\t",list(Defaults.keys()),ra=1)
    
        for k in Defaults.keys():
            if k not in Dst.keys():
                if Defaults[k] is REQUIRED:
                    cprint('*** Error. '+qtd('--'+k)+' is a required cmd line arg. ***','white','on_red')
                    print_dic_simple(Defaults,'Defaults')
                    os.sys.exit()
                else:
                    Dst[k] = Defaults[k]
    
    
    def advance(lst,e,min_len=1):
        len_lst = len(lst)
        if len_lst < min_len:
            pass
        elif len_lst > 1.2*min_len:
            lst = lst[-min_len:]
        else:
            lst.pop(0)
        lst.append(e)
    
    
    def a_key(dic):
        keys = dic.keys()
        k = np.random.randint(len(keys))
        return keys[k]
    
    
    def an_element(dic):
        return dic[a_key(dic)]
    
    
    
    
    def files_to_dict(path,D={}):
        D['.'] = []
    
        fs = sggo(path,'*')
        for f in fs:
            if not os.path.isdir(f):
                D['.'].append(fname(f))
            else:
                D[fname(f)] = files_to_dict(f,{})
        return D



if False:
    def __di(path,e=None):
        assert type(path) == str
        kc = path.split('/')
        return da(*kc,e=e)
        

    def __da(
            *kc,
            D=ENV.D,
            e=None,
            num_tuple_to_num=True,
        ):
        if e is None:
            return use_keychain(kc,D,num_tuple_to_num)
        else:
            set_with_keychain(kc,D,e,num_tuple_to_num)






    def use_keychain(kc,D,num_tuple_to_num=True):
        if num_tuple_to_num:
            kc = _untuple_keychain(kc)   
        for k in kc:
            D = D[k]
        return D


    def set_with_keychain(kc,D,e,num_tuple_to_num=True):
        if num_tuple_to_num:
            kc = _untuple_keychain(kc)
        for i in range(len(kc)-1):
            k = kc[i]
            if type(k) is tuple and len(k) == 1:
                k = k[0]
            D = D[k]
        D[kc[-1]] = e

    def _untuple_keychain(kc):
        kc_ = []
        for k in kc:
            if type(k) is tuple and len(k) == 1:
                k = k[0]
            kc_.append(k)
        return kc_ 
#EOF
