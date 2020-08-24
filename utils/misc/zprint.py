
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



def get_j_and_W(
    item,
    t='',
    j=0,
    r=0,
    p=0,
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

        
        if j in _W:
            cE(j,'in',kys(_W))
        else:
            pass
        assert j not in _W

        _W[j] = _keylist_

        if t is not None and type(t) is not tuple:
            name = str(t)
        elif type(t) is tuple and len(t) == 1:
            name = d2n('(',t[0],')')
        else:
            name = t

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
            j,_ = get_j_and_W(
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

    else:
        pass

    return j,_W



def preprocess(Q):

    for k in kys(Q):

        if type(Q[k]) is list:
            D = {}
            for i in rlen(Q[k]):
                D[(i,)] = Q[k][i]
            Q[k] = D

        if type(Q[k]) is dict:
            Q[k] = preprocess(Q[k])

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



def post_process(Din, html=False):

    D = Din.copy()

    if html:
        space_char = '&nbsp'
        line_end = ' <br>'
    else:
        space_char = ' '
        line_end = ''
    vert =  '|ssss'
    blank = 'sssss'
    bend =  '────┐'
    blank = blank.replace('s',space_char)
    vert = vert.replace('s',space_char)
    
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
        print(''.join(w)+line_end)

    return D


def zprint(
    Dictionary,
    t='',
    j=0,
    r=0,
    p=0,
    ignore_keys=[],
    only_keys=[],
    ignore_types=[],
    max_items=999999,
    html=False,
):

    V = preprocess( Dictionary )

    _,D = get_j_and_W(
        V,
        t=t,
        j=j,
        ignore_keys=ignore_keys,
        only_keys=only_keys,
        ignore_types=ignore_types,
        max_items=max_items,
    )

    E = post_process( D, html=html )

    if p:
        time.sleep(p)

    if r:
        raw_enter()

    return V,D,E


if __name__ == '__main__':

    A = get_Arguments(Defaults={'eg':0,'html':False})

    R = {
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

    J = {
        'A':{
            'B':{'G':{'a':'Big is beautiful!'},'H':'holy cow!',},    
            'I':{'G':[1,2,3],'H':[4,5,'6',(1,2)],}, 
        },
        'B':{
            'B':{'G':{'a':'Big is beautiful!'},'H':'holy cow!',},    
            'I':{'G':[1,2,3],'H':[4,5,'6',(1,2)],}, 
        },
    }

    Egs = [R, J]

    V,D,E = zprint(Egs[A['eg']],html=A['html'])

#EOF




