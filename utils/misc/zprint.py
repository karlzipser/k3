
from k3.utils.misc.printing import *

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
):

    title = t

    item_printed = False

    if type(item) in ignore_types:
        return

    if type(title) not in [str,type(None)]:
        title = str(title)

    lst = []

    for i in range(len(space_increment)):
        lst.append('.')

    lst.append('.')

    indent_text = ''.join(lst)

    n_equals = ''

    if numbering:
        if type(item) in [dict,list]:
            n_equals = cf(' (n=',len(item),')','`w-d',s0='',s1='')

    if title != None:

        if len(title) > len(indent_text):
            indent_title = title
        else:
            indent_title = title + indent_text[len(title):]

        if type(item) in [dict,list]:
            clp(spaces,'`',indent_title,'`',n_equals,s0='',s1='')
        else:
            clp(spaces,'`',title,'','`y',' ','`',item,'`g',s1='',s0='' )
            item_printed = True

    else:
        if type(item) in [dict,list]:
            clp(spaces,indent_text,n_equals,s0='',s1='')


    if type(item) == list:
        ctr = 0
        for i in item:
            zprint(i,t=None,spaces=spaces+space_increment,space_increment=space_increment,ignore_keys=ignore_keys,only_keys=only_keys,ignore_types=ignore_types,numbering=numbering)
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
            zprint(item[k],t=k,spaces=spaces+space_increment,space_increment=space_increment,ignore_keys=ignore_keys,only_keys=only_keys,ignore_types=ignore_types,numbering=numbering)
            ctr += 1
            if ctr >= max_items:
                break            
    elif not item_printed:
        color_print(spaces,item,'`g',s0='',s1='')

    if p:
        time.sleep(p)

    if r:
        raw_enter()


if __name__ == '__main__':
    Q = {
        '1':{
            '2':{
                '.meta':[5,6],
                'a':1,
            '7':{'xx':['a','v','r',[1,2,3]]},
            '8':'eight',
            }
        },
        'qqq':'zzz',
    }
    zprint(Q)
    
#EOF
