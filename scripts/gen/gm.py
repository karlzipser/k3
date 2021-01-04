#!/usr/bin/env python3

from k3.utils import *

record_PID(__file__,just_one=True)


A = get_Arguments(
    {
        ('p', 'place')  : 'drafts',
        ('n', 'search for name') : '',

    },
    verbose=True,
    file=__file__,
)

exec(A_to_vars_exec_str)

if p_ == '':
    url = "https://mail.google.com/mail/u/0/#search/NAME"

elif p_ == '':
    url = "https://mail.google.com/mail/u/0/#PLACE"

else:
    url = "https://mail.google.com/mail/u/0/#search/in%3APLACE+NAME"

url = url.replace(NAME,n_).replace(PLACE,p_)


os_system('open',url)

#EOF

