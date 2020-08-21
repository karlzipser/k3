#!/usr/bin/env python
from k3.utils import *

t = 1.

if 't' in Arguments:
    t = float(Arguments['t'])
print_Arguments()

nvidia_smi_continuous(t)

#EOF

    