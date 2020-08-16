from k3.vis3 import *
import k3.drafts.kimages.kimages_.jpeg as jpeg
import argparse

par = argparse.ArgumentParser(
    prog=__file__,
    description='display and rate from command line',
    fromfile_prefix_chars='@',
    add_help=True,
)
aa = par.add_argument
aa(
    '--src',
    action='store',
    type=str,
    default="Pictures/Photos Library.photoslibrary/originals", 
    help='src photos path',
)
aa(
    '--dst',
    action='store',
    type=str,
    default=opjD('Photos/all'),
    help='dst photos path',
)
args = par.parse_args()

Is = {}

ff = get_list_of_files_recursively(args.src,'*.jpeg',FILES_ONLY=True,ignore_underscore=False)



for f in ff:
    f = f[1:]
    Is[f] = jpeg.metadata(f,show=False)    
    U = jpeg.collect_essential_metadata(Is[f])
    new_name,new_dir = jpeg.new_name_dir(U)
    clp(f,'`r',new_name,'`g',new_dir,'`b',r=0)
    d = opj(args.dst,new_dir)
    os_system('mkdir -p',d,e=1)
    os_system('rsync -avL',qtd(f),qtd(opj(d,new_name)),e=1)

#EOF
