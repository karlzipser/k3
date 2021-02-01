
from k3.utils import *
from k3.utils.vis import *
import threading






if 'set up arguments and automatically named variables':

    A = get_Arguments(
        {
        	('path',"image search paths. if [], then select interactively") : [],
            ('name','name for new folder') : 'no_name',
            ('action','action to take on selected images') : 'ln',
            ('r','recursive image file search') : True,
            ('max','max number of images to permit') : 100,
            ('offset','offset within image list') : 0,
            ('ignore','folders to ignore') : ['Photos Library','Photo Booth'],
            ('start','start location for selecting') : opjh(),
            ('extent','image extent, less than one indicates no change') : 400,
            ('topic','map to topic') : '',
            ('filter','filter topics') : [],
            ('logic',"'and', 'or', or 'xor' for filters") : 'or',
            key_for+'quit' : 'q',
            key_for+'to beginning' : 'b',
            key_for+'to end' : 'e',
            key_for+'back' : ',',
            key_for+'forward' : '/',
            key_for+'to previous' : '<',
            key_for+'to next' : '?',
            key_for+'_act' : 'a',
            key_for+'select' : ' ',
            key_for+'un-select' : 'u',
            key_for+'notable' : '.',
            key_for+'not notable' : ';',
            key_for+'get action' : 'c',
            key_for+'get name' : 'n',
            key_for+'get topic' : 't',
            key_for+'topic toggle' : 'x',
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
        r=True,
    ); exec(A_to_vars_exec_str); del topic_






if 'utility functions':

    def _ready():
        print('\nHit <return> to continue...')
        getch()

    def _get_name(s='name'):
        _ready()
        name = get_safe_name(input('Enter '+s+' => '))
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
        l = name_#fname(A['paths'][0])
        l = re.sub("^.+\.--\.",'',l)
        if action_ == 'ln':
            a = 'ln.'
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
    Topics = {'notable':[],'ignore':[]}
    selected = []
    ts = sggo(opjb(fnamene(__file__),'*.topic.txt'))
    for t in ts:
        topic = fnamene(t)
        Topics[topic] = load_text_list(t,unique=True)

    if len(filter_) > 0:
        #cm(filter_)
        #kprint(Topics)
        fs = []
        for t in Topics:

            if t in filter_:
                fs += Topics[t]
        #cm(fs)
    else:
        fs = find_images_from_paths(path_,start=start_,recursive=r_)
        cm(fs)








if 'more setup':
    stp = 1
    i = 0
    _1 = get_terminal_size()[0]
    minus = _1 - 6
    plus = 3
    del _1


fs, _ = get_lists_of_paths(fs)
fs = list(set(fs)-set(Topics['ignore']))
fs = sorted(fs,key=natural_keys)
m = min(offset_+max_,len(fs))
fs = fs[offset_:offset_+m]
nimgs = len(fs)


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

def find_different_path(paths,i,positive=True):
    if i < 0 or i > len(paths):
        return 0
    p = pname(paths[i])

    if positive:
        rng = range(i,len(paths))
    else:
        rng = range(i,-1,-1)

    for j in rng:
        if pname(paths[j]) != p:
            return j

    return i


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
                Topics,#{'N':Topics['notable'],'S':selected,},
                colorize=True,
            )
            do_print = False
            topics = ['#']
            for k in Topics:
                if list_of_paths[i] in Topics[k]:
                    topics.append(k)
            if len(topics) > 2 and 'notable' in topics:
                topics.remove('notable')
            print(' '.join(topics))

        f = list_of_paths[i]

        k = display(f,Images=Images,extent=extent_,selected=selected,notable=Topics['notable'])

        h = handle_k(k,A)

        if  h == key_for+'quit':
            break

        elif h == key_for+'forward':
            i += stp
            if i >= nimgs:
                i = nimgs-1
            do_print = True

        elif h == key_for+'back':
            i -= stp
            if i < 0:
                i = 0
            do_print = True

        elif h == key_for+'to beginning':
            i = 0
            do_print = True

        elif h == key_for+'to end':
            i = nimgs-1
            do_print = True

        elif h == key_for+'to next':
            i = find_different_path(list_of_paths,i,positive=True)
            do_print = True

        elif h == key_for+'to previous':
            i = find_different_path(list_of_paths,i,positive=False)
            do_print = True

        elif key_for in h and 'step' in h:
            stp = int(A[h])

        elif h == key_for+'select':
            if f not in selected:
                selected.append(f)
                selected = sorted(selected,key=natural_keys)
                if A['topic'] not in Topics:
                    Topics[A['topic']] = []
                Topics[A['topic']].append(f)
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
                if A['topic'] in Topics:
                    Topics[A['topic']].remove(f)
            do_print = True

        elif h == key_for+'notable':
            if f not in Topics['notable']:
                Topics['notable'].append(f)
                Topics['notable'] = sorted(Topics['notable'],key=natural_keys)
            else:
                pass
            i += stp
            if i >= nimgs:
                i = nimgs-1
            do_print = True

        elif h == key_for+'not notable':
            #cm('here')
            if f not in Topics['notable']:
                #cm(0)
                pass
            else:
                #cm(1)
                Topics['notable'].remove(f)
            do_print = True

        elif h == key_for+'get name':
            name_ = _get_name()
            if name != '_':
                name = '_' + name
            A['name'] = name_

        elif h == key_for+'get topic':
            while len(selected):
                selected.pop()
            A['topic'] = _get_name('topic')

            
        elif h == key_for+'topic toggle':
            while len(selected):
                selected.pop()
            topics = sorted(kys(Topics),key=natural_keys)
            if not A['topic']:
                A['topic'] = topics[0]
            else:
                for ii in rlen(topics):
                    if topics[ii] == A['topic']:
                        jj = ii+1
                        if jj >= len(topics):
                            jj = 0
                        A['topic'] = topics[jj]
                        break
            print('topic =',A['topic'])

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
        for k in Topics:
            print('saving',k)
            ps = [
                opj(p,d2p('.'+k,time_str('FileSafe'),'topic.txt')),
                opj(p,k+'.topic.txt'),
            ]
            for q in ps:
                #print('saved',q)
                list_of_strings_to_txt_file(q,sorted(list(set(Topics[k])),key=natural_keys))
    except:
        cE('notable not saved')





Threader_state['done'] = True



#EOF
