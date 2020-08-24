
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


leaf = 'leaf|'

def zprint(
    item,
    t='',
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

    if False:#'lists':
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
            #clp(_spaces,'`',indent_name,'`',fj,s0='',s1='')
            j += 1

        else:
            
            #clp(_spaces,'`',str(name),'`','──','`',item,'`g',' ',fj,s1='',s0='' )
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
                    {'G':{'G':{'aaaaaa':'b'},'H':'h',},'H':'h',},
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
            'Ccccc':{
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

    Q = {
        'A':{
            'B':{'G':{'a':'Big is beautiful!'},'H':'holy cow!',},    
            'I':{'G':[1,2,3],'H':[4,5,'6',(1,2)],}, 
        },
        'B':{
            'B':{'G':{'a':'Big is beautiful!'},'H':'holy cow!',},    
            'I':{'G':[1,2,3],'H':[4,5,'6',(1,2)],}, 
        },

    }

    def preprocess_Q(Q):

        for k in kys(Q):

            if type(Q[k]) is list:
                D = {}
                for i in rlen(Q[k]):
                    D[(i,)] = Q[k][i]
                Q[k] = D

            if type(Q[k]) is dict:
                Q[k] = preprocess_Q(Q[k])

            elif type(Q[k]) is None:
                pass

            else:
                if is_number(Q[k]):
                    s = cf(Q[k],'`g-b')
                elif type(Q[k]) is str:
                    s = cf(Q[k],'`y-b')
                else:
                    s = cf(Q[k],'`b-b')
                Q[k] = { leaf+s : None }
        return Q

    V = preprocess_Q(Q.copy())


    clear_screen()
    _,D = zprint(V)


    pprint(D)
    vert =  '|    '
    blank = '     '
    bend =  '────┐'
    
    max_width = 0
    for i in range(max(kys(D))):
        max_width = max(max_width,len(D[i]))

    for u  in range(max_width):
        for i in range(max(kys(D)),0,-1):
                try:
                    if D[i][u] == D[i+1][u]:
                        D[i+1][u] = vert
                except:
                    pass
        in_line = False
        for i in range(max(kys(D)),0,-1):

                try:
                    if D[i][u] != vert:
                        in_line = True
                    if not in_line and D[i][u] == vert:
                        D[i][u] = blank
                except:
                    in_line = False

    

    for θ in range(0,max(kys(D))+1):
        if len(D[θ]):
            if leaf in D[θ][-1]:
                D[θ][-1] = D[θ][-1].replace(leaf,'')
                continue
            l = len(D[θ][-1])
            if l <= len(bend):
                b = bend[l-1:]
            else:
                b = ''
            b += cf('',θ,'`--d')
            D[θ].append(b) #

    for θ in range(0,max(kys(D))+1):
        w = []
        for y in D[θ]:
            if type(y) is tuple:
                y = '•'
            w.append(str(y))
        print(''.join(w))



#EOF
