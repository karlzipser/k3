#!/usr/bin/env python3

from k3.utils import *

Arguments = get_Arguments({('at','a parameter to set'):REQUIRED,'b':2,'c':REQUIRED})

print_dic_simple(Arguments,title="Arguments")

#EOF
