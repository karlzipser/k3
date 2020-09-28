
from k3.utils.core import *
from k3.utils.dict.dict_access import *
from k3.utils.misc.sys import *
from k3.utils.misc.osx import *

Arguments = get_Arguments(
    Defaults={
        'path':'k3',
        'condense_dict':False,
        'ignore_meta':True,
        'max_depth':1,
    }
)

# python k3/utils/misc/file_menu.py --path /Users/karlzipser/Library/Mobile\ Documents/com\~apple\~CloudDocs/pictures --max_depth 9
    
def main(**Arguments):
    eg(__file__)

    name = Arguments['path']

    if name == 'history':

        D = {}
        oD = dict_access(D,name)

        def lines_from_hist_file(path):
            r = r'(^\s*\d+\s+)([\w\./\-].*)'
            q = []
            h = txt_file_to_list_of_strings(path)
            for l in h:
                m = re.match(r,l)
                if m:
                    #cy(m.groups()[1],r=1)
                    a = m.groups()[1]
                    #print(qtd(a))
                    a = re.sub(r'\s*$','',a)
                    #print(qtd(a))
                    a = re.sub(r'\s+',' ',a)
                    #print(qtd(a))
                    q.append(a)
                else:
                    cr(l,r=0)
            return q

        histfile = opjD('hist.txt')
        q = lines_from_hist_file(histfile)

        for p in q:
            try:
                oD( p.replace(' ','/') + '/' , e=p )
            except KeyboardInterrupt:
                cr('*** KeyboardInterrupt ***')
                sys.exit()
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print('Exception!')
                print(d2s(exc_type,file_name,exc_tb.tb_lineno)) 

        
    else:

        D = files_to_dict(opjh(name),D={})

        oD = dict_access(D,name)



    if Arguments['condense_dict']:
        D = condense_dict(D)

    close_Finder_windows()
    quit_Preview()

    navigate(D,oD,name,Arguments)


def navigate(D,oD,name,Arguments):

    if Arguments['ignore_meta']:
        oD('__meta__/ignore_keys/', e=['__meta__'])
    if Arguments['max_depth']:
        oD('__meta__/max_depth/', e=Arguments['max_depth'])

    clear_screen()
    oD(up_down='-')

    c = None

    U = {}

    while True:

        c = input('-> ')

        cc = '-'
        
        m = re.match( r'^\s*([a-z]+)\s*(\d*)$', c)

        if m:

            if m.groups()[0] == 'q':
                close_Finder_windows()
                quit_Preview()
                break

            elif m.groups()[0] == 'c':
                close_Finder_windows()
                quit_Preview()

            elif m and m.groups()[0] == 'm':
                cr(m.groups()[1], str_is_int(m.groups()[1]))
                if str_is_int(m.groups()[1]):
                    i = int(m.groups()[1])
                else:
                    i = input_int_in_range(
                        0,
                        10*10,
                        d2n('max depth (',D['__meta__']['max_depth'],') >>> ')
                    )
                if type(i) is int:
                    D['__meta__']['max_depth'] = i
                clear_screen()
                oD(up_down='-')
                continue
        
            elif m.groups()[0] in ['u','d']:
                cc = m.groups()[0]

        clear_screen()
        U,print_lines = oD(up_down=cc)
        
        m = re.match( r'^\s*(\d+)\s*(\w*)$', c)

        if m:
            if str_is_int(m.groups()[0]):
                i = int(m.groups()[0])

                if i in U:
                    p = U[i]['path']
                    oD('__meta__/menu_path/',e=p)

                    clear_screen()      
                    oD(up_down='-')

                    oDp = oD(p)

                    if type(oDp) is dict:
                        oDp_show = '{...}'
                        if len(m.groups()[1]) > 0:
                            if m.groups()[1] == 'o':
                                os_system('open',qtd(name+'/'+p))

                    elif type(oDp) is list:
                        
                        oDp_show = '' # '[...]'
                        if True:#len(m.groups()[1]) > 0:
                            #if m.groups()[1] == 'o':

                            rng = []

                            if U[i]['lst_indx'] is None:
                                if m.groups()[1] == 'o':
                                    rng = range(len(oDp))
                            else:
                                rng = [U[i]['lst_indx']]

                            for j in rng:
                                e = oDp[j]
                                n = qtd(name+'/'+p+e)
                                cg(qtd(exname(e.lower())))
                                if exname(e.lower()) in [
                                    '',
                                    'txt','rtf','xml','html','doc',
                                    'py','c','cpp','c++',
                                    'jpg','jpeg',
                                    'png',
                                    'gif','giff',
                                    'tiff','tif',
                                ]:
                                    os_system('open',n)
                                else:
                                    if exname(e) != 'pyc':
                                        cr(
                                            'ignorning',
                                            n,
                                            'because of extension'
                                            )
                    elif type(oDp) is tuple:
                        oDp_show = '(...)'
                    elif type(oDp) is str:
                        oDp_show = oDp
                        os_system('open',qtd(name+'/'+out_))
                    else:
                        oDp_show = str(oDp)

                    
                    if U[i]['lst_indx'] is None:
                        out_ = p + oDp_show
                        cy('out:',out_)
                    else:
                        out_ = p+str(oDp[U[i]['lst_indx']])
                        cg('out:',out_)










if not interactive() and __name__ == '__main__':
    main(**Arguments)



#EOF

# ,b



