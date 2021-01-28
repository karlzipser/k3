
from k3.utils import *
from k3.utils.vis import *
import threading






if 'set up arguments and automatically named variables':

    A = get_Arguments(
        {
        	('paths',"image search paths. if [], then select interactively"):[],
            ('path','single path instead of paths') : '',
            ('name','name for new folder'):'no_name',
            ('action','action to take on selected images') : 'ln',
            ('r','recursive image file search') : True,
            ('max','max number of images to permit') : 100,
            ('offset','offset within image list') : 0,
            ('ignore','folders to ignore') : ['Photos Library','Photo Booth'],
            ('start','start location for selecting') : opjh(),
            ('extent','image extent, less than one indicates no change') : 400,
            ('notable','use list of notable images') : False,
            key_for+'quit' : 'q',
            key_for+'back' : ',',
            key_for+'forward' : '/',
            key_for+'_act' : 'a',
            key_for+'select' : ' ',
            key_for+'un-select' : 'u',
            key_for+'notable' : '.',
            key_for+'not notable' : ';',
            key_for+'get action' : 'A',
            key_for+'get name' : 'N',
            key_for+'1 step' : '1',
            key_for+'2 step' : '2',
            key_for+'3 step' : '3',
            key_for+'4 step' : '4',
            key_for+'5 step' : '5',
            key_for+'6 step' : '6',
            key_for+'7 step' : '7',
            key_for+'8 step' : '8',
            key_for+'9 step' : '9',
        },
        file=__file__,
        r=False,
    ); exec(A_to_vars_exec_str)






if 'utility functions':

    def _ready():
        print('\nHit <return> to continue...')
        getch()

    def _get_name():
        _ready()
        name = get_safe_name(input('Enter name => '))
        if name != '_':
            name = '_' + name
        print(qtd(name))
        return name

    def _get_action():
        _ready()
        a = get_safe_name(input('Enter action => '))
        if a not in ['cp','ln','mv']:
            cE(qtd(a),"is not in ['cp','ln','mv'[")
            return ''
        else:
            return a

    def _act():
        l = fname(paths_)
        l = re.sub("^.+\.--\.",'',l)
        if action_ == 'links':
            a = 'links.'
        else:
            a = ''
        l = d2n(a,time_str('FileSafe'),'.--.',l )
        if name_ != '':
            l = '_' + name_ + '.' + l
        else:
            l = '_' + l
        links_ = opjD(l)
        os_system('mkdir -p',qtd(d2p(links_,A['name'])),e=1)
        real_paths = []
        for f in selected:
            if action_ == 'ln':
                os_system('ln -s',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']),fname(f))),e=1,a=1)
            elif action_ == 'cp':
                os_system('cp',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']))),e=1,a=1)
            elif action_ == 'mv':
                os_system('mv',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']))),e=1,a=1)
            real_paths.append(os.path.realpath(f))
            list_of_strings_to_txt_file(opjD(d2p('paths',A['name'],'txt')),real_paths)






if 'find image files':
    selected = []
    notable = load_text_list(opjb(fnamene(__file__),'notable.txt'))
    if notable_:
        fs = notable
    else:
        if path_ != '':
            assert paths_ == []
            paths_ = [path_]
            path_ = ''
        #fs = find_images_from_paths(paths_)
        fs = find_images_from_paths(paths_,start=start_,recursive=r_)
    fs = sorted(fs,key=natural_keys)
    m = min(offset_+max_,len(fs))
    fs = fs[offset_:offset_+m]
    nimgs = len(fs)













if 'more setup':
    stp = 1
    i = 0
    _1 = get_terminal_size()[0]
    minus = _1 - 6
    plus = 3
    del _1






list_of_paths, blanked_list_of_paths = get_lists_of_paths(fs)


if 'set up loader thread':
    Images = {}
    Threader_state = {            
        'Images':Images,
        'done':False,
        'fs':list_of_paths,
        'extent':extent_,
    }
    threading.Thread(
        target=image_loader_thread,
        args=(Threader_state,),
    ).start()



#print_list_segment(list_of_paths,blanked_list_of_paths,i,minus,plus)



do_print = True


if 'main loop':

    while True:

        if do_print:
            print_list_segment(
                list_of_paths,
                blanked_list_of_paths,
                i,
                minus,
                plus,
                {'N':notable,'S':selected,},
            )
            do_print = False

        f = list_of_paths[i]

        k = display(f,Images=Images,extent=extent_,selected=selected,notable=notable)

        h = handle_k(k,A)

        if  h == key_for+'quit':
            break

        elif h == key_for+'forward':
            i += stp
            if i >= nimgs:
                i = nimgs-1
            #clear_screen()
            do_print = True

        elif h == key_for+'back':
            i -= stp
            if i < 0:
                i = 0
            #clear_screen()
            #print_list_segment(list_of_paths,blanked_list_of_paths,i,minus,plus)
            do_print = True

        elif key_for in h and 'step' in h:
            stp = int(A[h])

        elif h == key_for+'select':
            if f not in selected:
                selected.append(f)
                selected = sorted(selected,key=natural_keys)
            else:
                pass
            i += stp
            if i >= nimgs:
                i = nimgs-1
            do_print = True
            
        elif h == key_for+'un-select':
            if f not in selected:
                pass
            else:
                selected.remove(f)
            do_print = True

        elif h == key_for+'notable':
            if f not in notable:
                notable.append(f)
                notable = sorted(notable,key=natural_keys)
            else:
                pass
            i += stp
            if i >= nimgs:
                i = nimgs-1
            do_print = True

        elif h == key_for+'not notable':
            cm('here')
            if f not in notable:
                cm(0)
                pass
            else:
                cm(1)
                notable.remove(f)
            do_print = True

        elif h == key_for+'get name':
            A['name'] = _get_name()
            name_ = A['name']

        elif h == key_for+'get action':
            a = _get_action()
            if len(a) > 0:
                A['action'] = a
                action_ = A['action']
                
        elif h == key_for+'_act':
            _act()
            break

    'end while'






if 'save notable paths':
    try:
        p = opjb(fnamene(__file__))
        os_system('mkdir -p',p)
        ps = [
            opj(p,d2p('notable',time_str('FileSafe'),'txt')),
            opj(p,'notable.txt'),
        ]
        for q in ps:
            print('saved',q)
            list_of_strings_to_txt_file(q,notable)
    except:
        cE('notable not saved')





Threader_state['done'] = True



#EOF
