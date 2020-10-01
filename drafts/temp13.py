from k3 import *
ps = ['k3/drafts/temp12.py']
I = {};exec(get_import_str(ps,I))


_Arguments = a2d("1 2 3 --pn True --test iqv")

def main(**A):
    s = ''
    s += boxed(d2s('\n'+__file__),'file') +'\n'
    s += boxed(print_dic_simple(A,print_=False),'_Arguments') +'\n'
    val = temp12(a=1.1,b=2.2,pn=A['pn'])   
    s += d2s('return value =',dp(val)) +'\n'
    return {
        'val':val,
        'str':s,
    }
    
if __name__ == '__main__':
    clear_screen()
    R = main(**_Arguments)
    box(
        d2n(
            
            boxed(R['str'],'str'),
            '\n',
            boxed(dp(R['val']),'val')
        ),
        'input/output'
    )

#EOF
  
