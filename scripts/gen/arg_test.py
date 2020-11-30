#!/usr/bin/env python3

from k3.utils import *

Arguments = get_Arguments({
	('asp','a parameter') : str,
	('b', 'who knows?')   : float,
	('c','just c')        : int,
	('d','a bool')        : bool,
})

print_dic_simple(Arguments, title="Arguments")

#EOF
