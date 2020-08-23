
from k3.utils.misc.printing import *
import copy

# https://pythonadventures.wordpress.com/2014/03/20/unicode-box-drawing-characters/

def format_j(j):
    assert(str_is_int(j))
    s = str(j)
    if len(s) == 1:
        s = s+' '

    s = cf(s,'`--d',' ')
    return s

def zprint(
    item,
    t='',
    spaces='',
    space_increment='    ',
    ignore_keys=[],
    only_keys=[],
    ignore_types=[],
    numbering=False,
    max_items=999999,
    r=0,
    p=0,
    j=0,
    K={},
):

    name = t

    kl=[]

    item_printed = False

    if type(item) in ignore_types:
        return

    if type(name) not in [str,type(None)]:
        name = str(name)

    lst = ['']

    for i in range(len(space_increment)-1):
        lst.append('─')

    lst.append('┐')

    if name == None:
        lst[0] = '└'

    indent_text = ''.join(lst)

    n_equals = ''

    if numbering:
        if type(item) in [dict,list]:
            n_equals = cf(' (n=',len(item),')','`w-d',s0='',s1='')

    if name != None:
        
        if len(name) > len(indent_text):
            indent_name = name
        else:
            indent_name = name + indent_text[len(name):]

        if type(item) in [dict,list]:
            clp(spaces,'`',indent_name,'`',n_equals,format_j(j),s0='',s1='')
            j += 1
        else:
            clp(spaces,'`',name,'','`','──','`',item,'`g',' ',format_j(j),s1='',s0='' )
            item_printed = True
            j += 1
        
    else:
        if type(item) in [dict,list]:
            clp(spaces,indent_text,n_equals,format_j(j),s0='',s1='')
            j += 1

    kl__ = []
    if type(item) == list:
        ctr = 0
        for i in item:
            j,kl_ = zprint(
                i,
                t=None,
                spaces=spaces+space_increment,
                space_increment=space_increment,
                ignore_keys=ignore_keys,
                only_keys=only_keys,
                ignore_types=ignore_types,
                numbering=numbering,
                j=j,
                K=K,
            )
            kl__ += kl_
            ctr += 1
            if ctr >= max_items:
                break
        kl.append(kl__)
        cr(j in K)
        K[j] = copy.deepcopy(kl)
        cb(j)
    elif type(item) == dict:
        
        ctr = 0
        for k in sorted(item.keys()):
            if k in ignore_keys:
                continue
            if len(only_keys) > 0:
                if k not in only_keys:
                    continue
            if type(item[k]) in [dict,list]:
                l = len(item[k])
            else:
                l = 1
            j,kl_ = zprint(
                item[k],
                t=k,
                spaces=spaces+space_increment,
                space_increment=space_increment,
                ignore_keys=ignore_keys,
                only_keys=only_keys,
                ignore_types=ignore_types,
                numbering=numbering,
                j=j,
                K=K,
            )
            kl__ += kl_

            ctr += 1
            if ctr >= max_items:
                break
        kl.append(kl__)
        cm(j in K)  
        K[j] = copy.deepcopy(kl)
        cy(j)

    elif not item_printed:
        cf(spaces,item,'`g',s0='',s1='')

    

    if p:
        time.sleep(p)

    if r:
        raw_enter()

    if name is not None:
        kl.insert(0,name)
    
    return j,kl


if __name__ == '__main__':
    Q = {
        'A':{
            'B':[
                    {'G':'g','H':'h',},
                    {'E':'e','F':'f',},
                ],
            'I':'i',
        },
        'C':'c',
    }
    Q_ = {
        'B':{
            'E':'e',
            'F':'f',
        }
    }
    K = {}
    j,kl = zprint(Q,t='TOP',K=K)
    #kprint(kl,'kl')
    #pprint(kl)
    #kprint(K,'K')
    K_ = {}
    cmax = max(K.keys())
    for k in K:
        K_[cmax-k] = K[k]
    del K
    K = K_
    kprint(K,'K',numbering=False)

#EOF
