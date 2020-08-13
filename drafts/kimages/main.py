
from k3.vis3 import *
from kimages_.utils import *
import kimages_.loop as loop
import kimages_.arguments as arguments

args = arguments.get_args()

kprint(vars(args),r=0)

if args.cmd_lines:
    print_command_lines(L)
    sys.exit()

L = setup_L(args)

save_L(L,args)

if args.hist:
    hist_L(L)

change = False


IMAGE_DIC = {}
reset_IMAGE_DIC(IMAGE_DIC,L,args)


threading.Thread(target=read_image_to_IMAGE_DIC,args=(IMAGE_DIC,)).start()


i_prev =  -1

while IMAGE_DIC['ctr'] < len(IMAGE_DIC['lst']):

    if timer.save.check() and change:
        save_L(L,args)
        timer.save.reset()

    if args.slideshow and timer.slideshow.check():
        reset_IMAGE_DIC(IMAGE_DIC,L,args)
        i = 0
        timer.slideshow.reset()

    i_save = IMAGE_DIC['ctr']

    use_exceptions = False

    if use_exceptions:

        try:   
            
            IMAGE_DIC['ctr'],i_prev,change = loop.body(IMAGE_DIC['ctr'],i_prev,change,IMAGE_DIC,L,args)
            

        except KeyboardInterrupt:
            cr('*** KeyboardInterrupt ***')
            IMAGE_DIC['del_lst'] = None
            if change:
                save_L(L)
            sys.exit()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Exception!')
            print(d2s(exc_type,file_name,exc_tb.tb_lineno))
            IMAGE_DIC['ctr'] += 1

    else:

        IMAGE_DIC['ctr'],i_prev,change = loop.body(IMAGE_DIC['ctr'],i_prev,change,IMAGE_DIC,L,args)
        if IMAGE_DIC['ctr'] == 'quit':
            IMAGE_DIC['del_lst'] = None
            break


    
if change:
    save_L(L,args)
   
#time.sleep(0.1) 


cg('Done.')



#EOF

