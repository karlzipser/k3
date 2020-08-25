
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
                D[y][m][g]['un'] = []
                for j in h:
                    if os.path.isfile(j):
                        D[y][m][g]['un'].append(j.split('/')[-1])
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
    use_color=0,
    ignore_keys=[],
    only_keys=[],
    ignore_types=[],
    max_items=999999,
    _top=True,
    _spaces='',
    _space_increment='    ',
    _W={},
    _keylist=[],
    depth=0,
    max_depth=0,
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
        if depth < max_depth:
            depth += 1
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
                    use_color=use_color,
                    _top=False,
                    _spaces=_spaces+_space_increment,
                    _space_increment=_space_increment,
                    ignore_keys=ignore_keys,
                    only_keys=only_keys,
                    ignore_types=ignore_types,
                    j=j,
                    _W=_W,
                    _keylist=_keylist_,
                    depth=depth,
                    max_depth=max_depth,
                )
                ctr += 1
                if ctr >= max_items:
                    break
    else:
        pass

    return j,_W



def preprocess(Q,use_color):

    for k in kys(Q):

        if type(Q[k]) is list:
            D = {}
            for i in rlen(Q[k]):
                D[(i,)] = Q[k][i]
            Q[k] = D

        if type(Q[k]) is dict:
            Q[k] = preprocess(Q[k],use_color)

        elif type(Q[k]) is None:
            pass

        else:
            if use_color:
                if is_number(Q[k]):
                    s = cf(Q[k],'`g-b')
                elif type(Q[k]) is str:
                    s = cf(Q[k],'`y-b')
                else:
                    s = cf(Q[k],'`b-b')
            else:
                s = str(Q[k])
            Q[k] = { leaf+s : None }
    return Q



def post_process(Din,use_line_numbers,use_color):

    D = copy.deepcopy(Din)

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
            if use_line_numbers:
                if use_color:
                    b += cf('',i,'`--d')
                else:
                    b += ' '+str(i)
            D[i].append(b)

    print_lines = []
    for i in range(0,max(kys(D))+1):
        w = []
        for y in D[i]:
            if type(y) is tuple:
                y = '└'# '•'
            w.append(str(y))
        print_lines.append(''.join(w))





    return D, print_lines


def zprint(
    Dictionary,
    t='',
    r=0,
    p=0,
    use_color=0,
    use_line_numbers=0,
    ignore_keys=[],
    only_keys=[],
    ignore_types=[],
    max_items=999999,
    max_depth=999999,
):

    V = preprocess( copy.deepcopy(Dictionary), use_color )

    _,D = get_j_and_W(
        copy.deepcopy(V),
        t=t,
        #j=j,
        ignore_keys=ignore_keys,
        only_keys=only_keys,
        ignore_types=ignore_types,
        max_items=max_items,
        max_depth=max_depth,
    )



    E,print_lines = post_process( copy.deepcopy(D), use_line_numbers, use_color )

    for i in rlen(D):
        #print(i,D[i])
        try:
            #cm(D[i][-1])
            if leaf in D[i][-1]:
                D[i] = D[i][:-1]
        except:
            pass
        for j in rlen(D[i]):
            if type(D[i][j]) == tuple and len(D[i][j]) == 1:
                D[i][j] = D[i][j][0]

    print('\n'.join(print_lines))

    if p:
        time.sleep(p)

    if r:
        raw_enter()

    return D,print_lines











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
                    {'aa':{'G':'g','G':'g','H':1,}},
                    {'bb':{'E':'e','F':('a',1),}},
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

    R = get_dictionary_of_Photos()

    D,print_lines = zprint(R,use_color=1,use_line_numbers=1,ignore_keys=[],max_depth=6)

    html_str = lines_to_html_str("""<p style="font-family: 'Courier New'">\n""",print_lines)
    text_to_file(opjD('n.html'),html_str)


#EOF




