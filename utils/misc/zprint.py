
from k3.utils.misc.printing import *


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

        if False:
        cm(_keylist)
        h = copy.deepcopy(_keylist)
        u = ['   ']
        if len(h) > 2:
            for e in h[:-2]:
                u.append('|')
                cy('   '.join(u)+'---')

    if 'init':

        if type(item) in ignore_types:
            return j,_W

        _keylist_ = copy.deepcopy(_keylist)

        if not _top:
            _keylist_.append(t)

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
        'D':{
            'C':{
                'B':[
                    {'aa':{'G':'g','H':'h',}},
                    {'bb':{'E':'e','F':'f',}},
                    {'cc':{'G':'g','H':'h',}},
                    {'dd':{'E':'e','F':'f',}},
                ],
                'I':'i',
            },
        }
    }
    
    clear_screen()

    _,_W = zprint(Q,_top=False,t='z')
    
    if False:

        kprint(_W)

        for i in list(_W.keys()):
            _keylist = _W[i]
            cg(i,_keylist)
            Q_ = extract_D(Q,_keylist)

            #kprint(Q_)




#EOF
