
from k3.utils.misc.printing import *

# https://www.ltg.ed.ac.uk/~richard/unicode-sample.html


top = opjD('Photos/all')
def get_dictionary_of_Photos():
    D = {}
    years = []
    a = sggo(top,'*')
    for b in a:
        years.append(b.split('/')[-1])
    for y in years:
        D[y] = {}
    for y in years:
        months = []
        c = sggo(top,y,'*')
        for d in c:
            months.append(d.split('/')[-1])
        for m in months:
            D[y][m] = {}
            days = []
            e = sggo(top,y,m,'*')
            for f in e:
                days.append(f.split('/')[-1])
            for g in days:
                h = sggo(top,y,m,g,'.meta/*')
                D[y][m][g] = {}
                D[y][m][g]['<unsorted>'] = []
                for j in h:
                    if os.path.isfile(j):
                        D[y][m][g]['<unsorted>'].append(j.split('/')[-1])
                    else:
                        D[y][m][g][fname(j)] = []
                        k = sggo(j,'*.jpeg')
                        for u in k:
                            D[y][m][g][fname(j)].append(u.split('/')[-1])
    return D



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
                s = cf(Q[k])#,'`g-b')
            elif type(Q[k]) is str:
                s = cf(Q[k])#,'`y-b')
            else:
                s = cf(Q[k])#,'`b-b')
            Q[k] = { leaf+s : None }
    return Q



def post_process(Din, html=False):

    D = copy.deepcopy(Din)

    if html:
        space_char = '&nbsp'
        line_end = ' <br>'
    else:
        space_char = ' '
        line_end = ''
    if not html:
        vert =  '|ssss'
        blank = 'sssss'
        bend =  '────┐'
    else:
        vert =  '|ssss'
        blank = 'sssss'
        bend =  ';&#9472;&#9472;&#9472;&#9472;&#9488;'

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

    for i in range(0,max(kys(D))+1):
        if len(D[i]):
            if leaf in D[i][-1]:
                D[i][-1] = D[i][-1].replace(leaf,'')
                continue
            l = len(D[i][-1])
            if l <= len(bend):
                b = bend[l-1:]
            else:
                b = ''
            #b += cf('',0)#,'`--d')
            D[i].append(b) #

    print_lines = []
    for i in range(0,max(kys(D))+1):
        w = []
        for y in D[i]:
            if type(y) is tuple:
                y = '└'# '•'
            w.append(str(y))
        print_lines.append(''.join(w)+line_end)

    print_str = '\n'.join(print_lines)

    return D, print_str


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

    V = preprocess( copy.deepcopy(Dictionary) )

    _,D = get_j_and_W(
        copy.deepcopy(V),
        t=t,
        j=j,
        ignore_keys=ignore_keys,
        only_keys=only_keys,
        ignore_types=ignore_types,
        max_items=max_items,
    )

    E,s = post_process( copy.deepcopy(D), html=html )

    print(s)

    if p:
        time.sleep(p)

    if r:
        raw_enter()

    return V,D,E,s


if __name__ == '__main__':

    A = get_Arguments(Defaults={'eg':0,'html':False})

    R = {
        'A':{
            'B':[
                    {'G':{'G':{'aaaaaa':'b'},'H':'h',},'H':'h',},
                    {'E':'e','F':'f',},
                ],
        
                'I':'i',
        },
        'X':{
            'B':[
                    {'G':'g','H':'h',},
                    {'E':'e','F':'f',},
                ],
            'I':'i',
            },
        'Q':{
            'Ccc':{
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
    #kprint(R)
    V,D,E,s = zprint(R,html=A['html'])

    
    h = s.replace(' ','&nbsp')
    h = h.replace('\n',' <br>\n')
    h = h.replace('─','&#9472;')
    h = h.replace('└','&#9492;')
    h = h.replace('┐','&#9488;')
    h = h.replace('[0m','')
    h = """<p style="font-family: 'Courier New'">\n""" + h
    text_to_file(opjD('n.html'),h)

"""
https://www.textfixer.com/html/convert-text-html.php

────┐
&#9472;&#9472;&#9472;&#9472;&#9488;


    if html:
        space_char = '&nbsp'
        line_end = ' <br>'
    else:
        space_char = ' '
        line_end = ''
    if not html:
        vert =  '|ssss'
        blank = 'sssss'
        bend =  '────┐'
    else:
        vert =  '|ssss'
        blank = 'sssss'
        bend =  ';&#9472;&#9472;&#9472;&#9472;&#9488;'
"""

#EOF




