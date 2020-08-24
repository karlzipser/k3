
from k3.utils.misc.printing import *

# https://www.ltg.ed.ac.uk/~richard/unicode-sample.html

def format_j(j):
    assert(str_is_int(j))
    s = str(j)
    if len(s) == 1:
        s = s+' '

    s = cf(s,'`--d',' ')
    return s




def kys(D):
    return list(D.keys())




def zprint(
    item,
    t='zprint()',
    r=0,
    p=0,
    j=0,
    ignore_keys=[],
    only_keys=[],
    ignore_types=[],
    max_items=999999,
    _top=True,
    _spaces='',
    _space_increment='    ',
    _W={},
    _keylist=[],
):
    if _top:
        _W = {}

    if False:
        _K[j-1] = copy.deepcopy(_keylist)


        if False:
            cb(j-1,_keylist,item)

            A,B = None,None
            if j-2 in _K:
                A = _K[j-2]
            B = _K[j-1]
            

            if B is not None and A is not None:

                for i in rlen(B):
                    try:
                        if A[i] == '|' or A[i] == B[i]:
                            B[i] = '|'

                        if A[0] == ' ':
                            B[0] = ' '
                        #if A[1] == ' ':
                        #    B[1] = ' '
                        if len(A) < len(B):
                            #if B[0] != ' ':
                            #    B[0] = ' '
                            #elif B[1] != ' ':
                            #    B[1] = ' '
                            pass
                    except:
                        pass


                cr('   '.join(B)+'───┐')

            #cb(n)

    if 'init':

        if type(item) in ignore_types:
            return j,_W

        _keylist_ = copy.deepcopy(_keylist)

        if not _top:
            _keylist_.append(t)
        #cm(_keylist_)
        
        if j in _W:
            cE(j,'in',kys(_W))
        else:
            pass#cg(j,list(_W.keys()))
        assert j not in _W

        _W[j] = _keylist_

        if t is not None and type(t) is not tuple:
            name = str(t)
        elif type(t) is tuple and len(t) == 1:
            name = d2n('(',t[0],')')
        else:
            name = t

    if 'lists':
        if type(item) is list:
            D = {}
            for i in rlen(item):
                D[(i,)] = item[i]
            item = D

    
    if 'formatting 1':

        item_printed = False

        lst = ['']

        for i in range(len(_space_increment)):
            lst.append('─')

        lst[-1] = '┐'

        if _top:
            name = cf(name,'`--u')

        indent_text = ''.join(lst)

        if _top:
            fj = ''
        else:
            fj = format_j(j)

        
        if len(str(name)) > len(indent_text):
            indent_name = name

        else:
            indent_name = str(name) + indent_text[(len(str(name))-1):]
            
        if type(item) is dict:
            clp(_spaces,'`',indent_name,'`',fj,s0='',s1='')
            j += 1

        else:
            clp(_spaces,'`',str(name),'`','──','`',item,'`g',' ',fj,s1='',s0='' )
            item_printed = True
            j += 1

    
    if type(item) == dict:
        
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
                _top=False,
                _spaces=_spaces+_space_increment,
                _space_increment=_space_increment,
                ignore_keys=ignore_keys,
                only_keys=only_keys,
                ignore_types=ignore_types,
                j=j,
                _W=_W,
                _keylist=_keylist_,

            )
            ctr += 1
            if ctr >= max_items:
                break


    elif not item_printed:
        cf(_spaces,item,'`g',s0='',s1='')

    else:
        pass


    if p:
        time.sleep(p)

    if r:
        raw_enter()

    return j,_W




def extract_D(Q,_keylist):
    if len(_keylist) == 0:
        return Q
    k = _keylist.pop(0)
    if type(k) is str:
        return extract_D(Q[k],_keylist)
    elif type(k) is tuple:
        return extract_D(Q[k[0]],_keylist)
    else:
        return Q

if __name__ == '__main__':
    Q = {
        'Π':{
            'B':[
                    {'G':{'G':{'a':'b'},'H':'h',},'H':'h',},
                    {'E':'e','F':'f',},
                ],
        
                'I':'i',
        },
        'Σ':{
            'B':[
                    {'G':'g','H':'h',},
                    {'E':'e','F':'f',},
                ],
            'I':'i',
            },
        'Φ':{
            'C':{
                'B':[
                    {'aa':{'G':'g','G':'g','H':'h',}},
                    {'bb':{'E':'e','F':'f',}},
                    {'cc':{'G':'g','H':'h',}},
                    {'dd':{'E':'e','F':'f',}},
                ],
                'I':'i',
            },
        }
    }
    Q__ = {
        'A':{
            'B':{'G':'g','H':'h',},    
            'I':{'G':'g','H':'h',}, 
        },
    }
    Q_ = {
        'A':{
            'B':{'G':{'a':'b'},'H':'h',},    
            'I':{'G':'g','H':'h',}, 
        },
    }

    clear_screen()
    _,_W = zprint(Q)#,_W={})

    if False:
        for r in range(10):
            clear_screen()
            _,_W = zprint(Q)
            a = input('> ')
            _keylist = _W[int(a)]
            Q_ = extract_D(Q,_keylist)
            zprint(Q_)
            raw_enter()

    if False:

        kprint(_W)

        for i in list(_W.keys()):
            _keylist = _W[i]
            a = input('> ')
            #cg(i,_keylist)
            #Q_ = extract_D(Q,_keylist)
            #zprint(Q_)

    pprint(_W)
    vert =  '|    '
    blank = '     '
    bend =  '────┐'
    for u  in range(6):
        for i in range(max(kys(_W)),0,-1):
                try:
                    if _W[i][u] == _W[i+1][u]:
                        _W[i+1][u] = vert
                except:
                    pass
        in_line = False
        for i in range(max(kys(_W)),0,-1):

                try:
                    if _W[i][u] != vert:
                        in_line = True
                    if not in_line and _W[i][u] == vert:
                        _W[i][u] = blank
                except:
                    in_line = False

    

    for θ in range(0,max(kys(_W))+1):
        _W[θ].append(bend) #

    for θ in range(0,max(kys(_W))+1):
        w = []
        for y in _W[θ]:
            if type(y) is tuple:
                y = cf((y[0]),'`y-d')
            w.append(str(y))
        print(''.join(w))

#EOF
