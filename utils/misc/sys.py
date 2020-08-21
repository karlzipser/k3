
from k3.utils.collections import *

def os_system(*args,e=0,r=0,a=1):
    s = d2s(*args)
    if(e):
        clp(s,r=r)
    elif r:
        raw_enter()
    if a:
        os.system(s)


def unix(command_line_str, print_stdout=False, print_stderr=False,print_cmd=False):
    command_line_str = command_line_str.replace('~',home_path)
    p = subprocess.Popen(command_line_str.split(), stdout=subprocess.PIPE)
    stdout,stderr = p.communicate()
    if print_cmd:
        print(command_line_str)
    if print_stdout:
        print(stdout)
    if print_stderr:
        print(stderr)
    s = stdout.decode("utf-8")
    return s.split('\n')





#EOF

