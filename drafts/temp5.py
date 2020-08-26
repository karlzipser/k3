from k3 import *

#,a

ENV = namedtuple('_', 'D')({})

def da(
        *kc,
        D=ENV.D,
        e=None,
        num_tuple_to_num=True,
    ):
    if e is None:
        return use_keychain(kc,D,num_tuple_to_num)
    else:
        set_with_keychain(kc,D,e,num_tuple_to_num)
#,b


words = ['cat','dog','mouse','horse']
MenuEg = {
    'range':{
        'min':{
            'current':0,
            'min':0,
            'max':10,
        },
        'max':{
            'current':10,
            'min':0,
            'max':10,
        },
    },
    'toggle':False,
    'word': {
        'current':words[-1],
        'options':words,
    }   
}

ENV.D['MenuEg'] = MenuEg

D, print_lines = zprint(
    ENV.D['MenuEg'],
    t='MenuEg',
    use_color=True,
    use_line_numbers=False,
    do_return=True,
    do_print=False,
)
#pprint(D)
#zprint(da('MenuEg','range'))

a = ['MenuEg','range']
curmax = a+['max','current']
maxmax = a+['max','max']
maxmin = a+['max','min']
curmin = a+['min','current']
minmax = a+['min','max']
minmin = a+['min','min']
tog = ['MenuEg','toggle']
a = ['MenuEg','word']
curword = a+['current']
woptions0 = a+['options',(0,)]
woptions1 = a+['options',(1,)]
woptions2 = a+['options',(2,)]
woptions3 = a+['options',(3,)]

#print(da(*curmax),da(*curmin))

for i in kys(D):
	if i+1 in D:
		if D[i] == D[i+1]:
			D[i+1].append('---')

V = {}
ctr = 1
for i in kys(D):
	if D[i] in [curmax,curmin,tog,woptions0,woptions1,woptions2,woptions3,]:
		V[ctr] = D[i]
		print_lines[i+1] += cf(' (',ctr,')','`m',s0='')
		ctr += 1
print('\n'.join(print_lines))
while True:
    c = int(input('> '))
    print(da(*V[c]))
#EOF