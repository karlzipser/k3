
import_list = ['os','os.path','shutil','scipy','scipy.io','string','glob','time','sys','datetime','random','re',
    'subprocess','threading','serial','inspect','fnmatch','h5py','socket','getpass','numbers','math']#,'importlib']

import_from_list = [['FROM','pprint','pprint'],['FROM','termcolor','cprint'],('FROM','collections','namedtuple')]

import_as_list = [['AS','numpy','np']]

    
for im in import_list + import_from_list + import_as_list:
    if type(im) == str:
        try:
            exec('import '+im)
        except:
            pass
            print('Failed to import '+im)
    else:
        assert type(im) == list or type(im) == tuple
        if im[0] == 'FROM':
            try:
                exec('from '+im[1]+' import '+im[2])
            except:
                pass
                print('Failed to from '+im[1]+' import '+im[2])
        else:
            assert(im[0] == 'AS')
            try:
                exec('import '+im[1]+' as '+im[2])
            except:
                pass
                print('Failed to import '+im[1]+' as '+im[2])           

try:
    import cPickle as pickle
except:
    import pickle


rnd = np.random.random
rndint = np.random.randint
rndn = np.random.randn
rndchoice = np.random.choice
na = np.array
host_name = socket.gethostname()
home_path = os.path.expanduser("~")
username = getpass.getuser()
degrees = np.degrees
arange = np.arange
shape = np.shape
randint = np.random.randint
randn = np.random.randn
zeros = np.zeros
ones = np.ones
reshape = np.reshape
mod = np.mod
array = np.array
sqrt = np.sqrt
sin = np.sin
cos = np.cos
sleep = time.sleep


_which_python = sys.version.split(' ')[0]
if _which_python[0] == '3':
    raw_input = input
    using_python3 = True
else:
    using_python3 = False

os.environ['PYTHONUNBUFFERED'] = '1'



#EOF