from k3 import *
import k3.aps.Menu.main as Menu_main

path = opjk() # i.e., use ~/k3/defaults.py for data

Q = Menu_main.start_Dic(
    dic_project_path=pname(path), 
    Arguments={
        'menu':False,
        'read_only':True,
    }
)
Q['load']()
T = Q['Q']

clp('from command line: ~/k3/Menu/main.py --path',path,'`--rb')

def sample_use_of_menu_data():

    while True:

        time.sleep(0.1)

        loaded = Q['load']()

        if loaded:
            clp(' '+time_str('Pretty')+' ','`ybb')
            pprint(T['State'])


if __name__ == '__main__':
    sample_use_of_menu_data()


#EOF
