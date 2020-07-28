from k3.utils.times import *
from k3.utils.files import *
from k3.utils.strings import *
from k3.utils.array_stuff import *
from k3.utils.clipcode import *
from k3.utils.connect import *

from k3.utils.more import *

log_name = get_safe_name(sys.argv[0].replace(opjk(),'')+'.txt')
log_strs = []
log_strs.append(' '.join(sys.argv).replace(opjk(),'')+' # '+time_str('Pretty'))
os.system('mkdir -p '+opjk('__local__','logs'))
list_of_strings_to_txt_file(opjk('__local__','logs',log_name),log_strs,write_mode="a")

#EOF