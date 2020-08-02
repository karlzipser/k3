from k3.utils3 import *

import argparse

par = argparse.ArgumentParser(
	prog='clp',
    description='use clp from command line',
    fromfile_prefix_chars='@',
    add_help=True,
    #allow_abbrev=False,
)

aa = par.add_argument

aa(
	'lst',
	nargs="+",
    help='space-separated list of things to print',
)

aa(
	'-v','--verbose',
    action='store_true',
    help='an optional argument',
   )

aa(
	'-r',
	action='store',
	type=int,
	required=False,
	default=0, 
	help='raw_enter',
)

args = par.parse_args()

print args

clp(*args.lst,r=args.r)
