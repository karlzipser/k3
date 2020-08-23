
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


saw_j,current_index,in_list = None,None,None

def zprint(
    item,
    t='zprint()',
    top=True,
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
    W={},
    keylist=[],
):

    global saw_j,current_index,in_list

    #cy(keylist)
    if len(keylist) > 1:
        #cm(2)
        if len(keylist[-1]) < len(keylist[-2]):
            cm(1)
            if type(keylist[-1]) is not tuple:
                cm(0)
                #if 'list_index' in keylist[-1][0]:
                saw_j = []
                current_index = -1
                #cE(current_index)
            else:
                cg(current_index)
    

    if len(W) == 0 :#or (
                #(len(keylist) > 0 and type(keylist[-1]) != tuple)):
                    #or
                #keylist[-1][0] != 'list_index' ):
        saw_j = []
        current_index = -1
        in_list = False

    name = t

    item_printed = False

    if type(item) in ignore_types:
        return j,W

    if type(name) not in [str,type(None)]:
        name = str(name)

    lst = ['']

    for i in range(len(space_increment)):
        lst.append('─')

    lst[-1] = '┐'

    if name == None:
        lst[0] = '└'
    elif top:
        name = cf(name,'`--u')

    indent_text = ''.join(lst)

    n_equals = ''

    if numbering:
        if type(item) in [dict,list]:
            n_equals = cf(' (n=',len(item),') ','`b-d',s0='',s1='')

    keylist_ = copy.deepcopy(keylist)


    if name is None:
        if j not in saw_j:
            saw_j.append(j)
            current_index += 1
        q = ('list_index',current_index)
    else:
        q = name

    if not top:
        keylist_.append(q)

    assert j not in W

    W[j] = keylist_

    
    if top:
        fj = ''
    else:
        fj = format_j(j)

    if name != None:
        
        if len(name) > len(indent_text):
            indent_name = name

        else:
            indent_name = name + indent_text[(len(name)-1):]
            
        if type(item) in [dict,list]:
            clp(spaces,'`',indent_name,'`',n_equals,fj,s0='',s1='')
            j += 1
            #print(0,qtd(indent_name))
        else:
            clp(spaces,'`',name,'`','──','`',item,'`g',' ',fj,s1='',s0='' )
            item_printed = True
            j += 1
            #print(1,qtd(name))
        
    else:
        if type(item) in [dict,list]:
            clp(spaces,indent_text,n_equals,fj,s0='',s1='')
            j += 1

    if type(item) == list:
        ctr = 0
        for i in item:
            j,_ = zprint(
                i,
                t=None,
                top=False,
                spaces=spaces+space_increment,
                space_increment=space_increment,
                ignore_keys=ignore_keys,
                only_keys=only_keys,
                ignore_types=ignore_types,
                numbering=numbering,
                j=j,
                W=W,
                keylist=keylist_,
            )

            ctr += 1
            if ctr >= max_items:
                break

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
            j,_ = zprint(
                item[k],
                t=k,
                top=False,
                spaces=spaces+space_increment,
                space_increment=space_increment,
                ignore_keys=ignore_keys,
                only_keys=only_keys,
                ignore_types=ignore_types,
                numbering=numbering,
                j=j,
                W=W,
                keylist=keylist_,
            )


            ctr += 1
            if ctr >= max_items:
                break


    elif not item_printed:
        cf(spaces,item,'`g',s0='',s1='')


    if p:
        time.sleep(p)

    if r:
        raw_enter()

    return j,W




def extract_D(Q,keylist):
    if len(keylist) == 0:
        return Q
    k = keylist.pop(0)
    if type(k) is str:
        return extract_D(Q[k],keylist)
    elif type(k) is tuple and k[0] == 'list_index':
        return extract_D(Q[k[1]],keylist)
    else:
        return Q

if __name__ == '__main__':
    Q = {
        'A':{
            'B':[
                    {'G':'g','H':'h',},
                    {'E':'e','F':'f',},
                ],
            'I':'i',
        },
        'C':{
            'B':[
                    {'G':'g','H':'h',},
                    {'E':'e','F':'f',},
                ],
            'I':'i',
        },
    }

    Q = {
        'A':{
            'B':{'G':'g','H':'h',},
            'I':'i',
        },
        'C':{
            'B':{10:{'G':'g','H':'h',},
                11:{'E':'e','F':'f',},
            },
            'I':'i',
        },
    }



    _,W = zprint(Q)

    if True:
        for i in list(W.keys()):
            keylist = W[i]
            cg(i,keylist)
            Q_ = extract_D(Q,keylist)

            pprint(Q_)




#EOF
