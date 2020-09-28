from k3.utils.core.essentials import *

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
std = np.std
pi = np.pi
sleep = time.sleep
sys = os.sys
gg = glob.glob

_Arguments = args_to_dict('face 1 2 -a a3 -b 4 1 a2 5 -c a12 1')

def main(**A):
    eg(__file__)
    print("cos(pi) =",cos(pi))
    print('home_path =',home_path)
    print('username =',username)
    print('host_name =',host_name)
    print('rndn(3) =',rndn(3))
    print_dic_simple(A)
    
if __name__ == '__main__':
    Arguments = get_Arguments(_Arguments)
    main(**Arguments)

#EOF
