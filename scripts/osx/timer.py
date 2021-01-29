
from k3.utils import *

A = get_Arguments(
    {
    	('t','time'):30,
        ('s','short time'):3,
        ('l','left'):False,
    },
    file=__file__,
    r=True,
); exec(A_to_vars_exec_str)


if l_:
    s = 'left'
else:
    s = 'right'
os_system('say',s)
os_system('say',qtd(d2s(t_,'seconds')))
os_system('say "ready set go!"')

timer = Timer(t_)
short_timer = Timer(s_)

while not timer.check():
    if short_timer.rcheck():
        os_system('say',qtd(d2s(int(timer.time()))))
    else:
        time.sleep(0.1)

os_system('say "stop!"')

#EOF
