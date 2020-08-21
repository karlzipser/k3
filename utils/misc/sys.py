
from k3.utils.misc.printing import *


def os_system(*args,e=0,r=0,a=1):
    s = d2s(*args)
    if(e):
        clp(s,'`--u')
    if a:
        os.system(s)
    if r:
        raw_enter()




def unix(command_line_str, print_stdout=False, print_stderr=False,print_cmd=False):

    command_line_str = command_line_str.replace('~',home_path)

    p = subprocess.Popen(command_line_str.split(), stdout=subprocess.PIPE)

    stdout,stderr = p.communicate()

    if type(stdout) == bytes:
        stdout = stdout.decode('utf8')

    if type(stderr) == bytes:
        stderr = stderr.decode('utf8')

    if print_cmd:
        clp('print_cmd:','`--u',command_line_str,'\n',)

    if print_stdout:
        clp('print_stdout:','`--u',stdout,'\n',)

    if print_stderr:

        clp('print_stderr:','`--u',stderr,'\n',)

    return stdout.split('\n')





if __name__ == '__main__':
    
    s = "os_system('ls',e=1,r=0)"

    clear_screen()
    clp('Example:',s,'`--r')

    exec(s)

    s = "o = unix('ls',True,True,True)"

    print('\n')
    clp('Example:',s,'`--r')

    exec(s)
    kprint(o,s+' # kprint of output',)

#EOF

