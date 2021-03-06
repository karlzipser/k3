
#,p2a
"""

python3 k3/aps/Learn/main_conv.py\
    --main 6\
    --net_str conv1\
    --save_output_2 True\
    --batch_size 1\
    --save_timer_time 999999\
    --LR 0.\
    --runs validate\
    --manual_input0 0\
    --GPU -1\
    --resume True\
    --graphics_timer_time 0\
    --backwards False\
    --single_run caffe_z2_direct_local_sidewalks_09Oct16_08h30m15s_Mr_Orange\
    --save_figures2 no\

"""
#,p2b

from k3 import *

import k3.aps.Learn.networks.net as networks_net
"""
import Menu.main
"""
from k3.aps.Learn.net_main_conv import Net_Main

USE_DISCRIMINATOR = False

"""
M = Menu.main.start_Dic(dic_project_path=pname(opjh(__file__)))
"""
M = {'Q':{
    'runtime_parameters':{
        'graphics_timer_time':-1,
        'abort':'_toggle',
        'graphics_ylim':[], #[0,0.1],
        'meo_num':8,
        'data_from_run':'no',#tegra-ubuntu_01Nov18_13h46m55s
        'data_from_ctr':-1,
        'data_from_flip':-1,
        'step':5,
        'ctr_reset':'_toggle',
        'save_images':False,
        'scale':2.0,
        'percent_loss_to_show':100,
        'loss_stds':8.0,
        'show_graphics':True,
    },
}}

"""
stat -c %Y kzpy3/.git/FETCH_HEAD

python k3/aps/Learn/main_conv.py --main 6 --net_str conv1  --save_output_2 0 --batch_size 1 --save_timer_time 999999 --runs train  --manual_input0 0 --GPU -1 --resume 0 --graphics_timer_time 0 --backwards 0

# 11/22/2020




    --save_figures2 jpeg\

"""

"""


caffe_z2_direct_Tilden_22Dec16_14h13m11s_Mr_Teal
direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow
direct_Tilden_LCR_15Jul17_10h52m51s_Mr_Yellow
direct_Tilden_LCR_15Jul17_12h29m14s_Mr_Yellow
direct_Tilden_LCR_23Jul17_10h27m34s_Mr_Yellow
direct_Tilden_LCR_24Jul17_17h13m40s_Mr_Yellow
"""


Net_strs = {

    'conv1' : """
        Learn 
            --type Conv,Fire3,conv1
            --resume True 
            --batch_size 64
            --save_timer_time 600 
            --target_offset 0 
            --input rgb
            --target outer_contours
            --losses_to_average 256 
            --runs train 
            --display.output 0,3 
            --display.input 0,3
            --display.target 0,3
            --clip 0.1
            --backwards True
            --win_x 20
            --win_y 40
            --drop 0.0
            --blue_center_button True
            --reset_loss False
            --momentum 0.0001
            --LR 0.001
            --hide_target_output_figure True
            --hide_loss True
            --hide_output_2 False
            --hide_meta True
            --hide_3d_output2 False
            --hide_3d_target True
    """,

    'conv0' : """
        Learn 
            --type Conv,Fire3,conv0
            --resume True 
            --batch_size 64
            --save_timer_time 600 
            --target_offset 0 
            --input rgb
            --target outer_contours
            --losses_to_average 256 
            --runs validate 
            --display.output 0,3 
            --display.input 0,3
            --display.target 0,3
            --clip 0.1
            --backwards True
            --win_x 20
            --win_y 40
            --drop 0.0
            --blue_center_button True
            --pts2_h5py_type h5py_angles0
            --reset_loss False
            --momentum 0.0001
            --LR 0.001
    """,
}

def main6():

    import torch
    import torch.nn as nn
    import torch.nn.parallel
    import torch.backends.cudnn as cudnn
    import torch.optim as optim
    import torch.utils.data
    import torchvision.datasets as dset
    import torchvision.transforms as transforms
    import torchvision.utils as vutils
    import torch.nn.utils as nnutils

    if USE_DISCRIMINATOR:
        from .discriminator1 import Discriminator,weights_init

    if 'net_str' in list(Arguments.keys()):
        clp('   FROM SYS_STR   ','`ybb',ra=False,p=1)
        Nets = {
            'N0':Net_Main(M=M,sys_str=Net_strs[Arguments['net_str']].replace('\n',' ').replace('\t',' '),Arguments_=Arguments),
        }
    else:
        assert(False)
        clp('   FROM COMMMAND LINE   ','`ybb',ra=False,p=1)
        Nets = {
            'N0':Net_Main(M=M,Arguments_=Arguments),
        }

    n = 'N0'
    Data = networks_net.make_batch( Nets[n]['get_data_function'], Nets[n]['P'], Nets[n]['P']['batch_size'] )
    cg('Data',shape(Data['input']),shape(Data['target']))


    if USE_DISCRIMINATOR:
        DISCRIMINATOR = Discriminator(nc=shape(Data['target'])[1]).cuda()


    if USE_DISCRIMINATOR:
        DISCRIMINATOR.apply(weights_init)

    criterion = nn.BCELoss()
    if USE_DISCRIMINATOR:
        optimizerD = optim.Adam(DISCRIMINATOR.parameters(), lr=0.01, betas=(0.5, 0.999))



    run_timer = Timer()
    freq_timer = Timer(30)

    if False:
        Abort = Toggler()

    wait_timer = Timer(5)

    minute_timer = Timer(60)

    if USE_DISCRIMINATOR:
        try:
            if Nets['N0']['P']['resume']:
                DISCRIMINATOR.load(Nets['N0']['P']['NETWORK_OUTPUT_FOLDER']+'.dcgan')
        except:
            clp("*** DISCRIMINATOR.load(Nets[n]['P']['NETWORK_OUTPUT_FOLDER']+'.dcgan') failed ***",ra=True)


    graphics_on = False


    while True:

        if False: M['load']()

        if False and Abort['test'](M['Q']['runtime_parameters']['abort']):
            break

        if False:#minute_timer.check():
            minute_timer.reset()
            Nets['N0']['P']['clip'] = float(Nets['N0']['P']['clip'])

            Nets['N0']['P']['clip'] *= 0.98
            clp('clip',Nets['N0']['P']['clip'],int(run_timer.time()),"`yb")


        
        GENERATOR = Nets[n]['N']
        Nets[n]['P']['original_Fire3_scaling'] = True

        if True:
            for k in list(M['Q']['runtime_parameters'].keys()):
                Nets[n]['P']['runtime_parameters'][k] = M['Q']['runtime_parameters'][k]

        Data = networks_net.make_batch( Nets[n]['get_data_function'], Nets[n]['P'], Nets[n]['P']['batch_size'] )

        if USE_DISCRIMINATOR:
            DISCRIMINATOR.zero_grad() 
            real = Data['target'][:,:,:,:] 
            label = torch.full((Nets[n]['P']['batch_size'],), 1,).cuda() 
            output = DISCRIMINATOR(torch.from_numpy(real).cuda().float()) 

            errD_real = criterion(output, label) 
            errD_real.backward() 
            D_x = output.mean().item() 

        GENERATOR.forward_no_loss(Data)
            
        if USE_DISCRIMINATOR:
            fake = GENERATOR.A['output'][:,:,:,:]
            label.fill_(0)
            output = DISCRIMINATOR(fake.detach()) 
            errD_fake = criterion(output, label) 
            errD_fake.backward() 
            D_G_z1 = output.mean().item() 
            errD = errD_real + errD_fake 
            optimizerD.step() 
        
        GENERATOR.optimizer.zero_grad()

        if Nets[n]['P']['runs'] == 'validate':
            pass
            #cb('validate')

        else:

            if USE_DISCRIMINATOR:
                label.fill_(1) 
                output = DISCRIMINATOR(fake) 
                if 's' not in Nets[n]['P']:
                    s = 0.0001
                else:
                    s = Nets[n]['P']['s']

                GENERATOR.loss = s*GENERATOR.criterion(GENERATOR.A['output'],GENERATOR.A['target']) + (1-s) * criterion(output, label) #19

            else:
                s = 1.0
                #cm(1,ra=1)
                #cm(GENERATOR.A['output_2'].size(),GENERATOR.A['target'].size(),ra=1)
                GENERATOR.loss = s*GENERATOR.criterion(GENERATOR.A['output_2'],GENERATOR.A['target'])

            if Nets[n]['P']['backwards']:
                GENERATOR.loss.backward() #20
                nnutils.clip_grad_norm(GENERATOR.parameters(), Nets['N0']['P']['clip'])
                GENERATOR.optimizer.step() #21

            GENERATOR.losses_to_average.append(GENERATOR.extract('loss'))
            if len(GENERATOR.losses_to_average) >= GENERATOR.num_losses_to_average:
                GENERATOR.losses.append( na(GENERATOR.losses_to_average).mean() )
                GENERATOR.losses_to_average = []


            if USE_DISCRIMINATOR:
                if GENERATOR.save():
                    DISCRIMINATOR.save(Nets[n]['P']['NETWORK_OUTPUT_FOLDER']+'.dcgan')
            else:
                GENERATOR.save()



        if True:#try:
            
            if Nets['N0']['P']['runtime_parameters']['show_graphics']:
                if not graphics_on:
                    clp('turning graphics on')
                graphics_on = True
                Nets[n]['graphics_function'](Nets[n]['N'],M,Nets[n]['P']) # graphics can cause an error with remote login
            else:
                if graphics_on:
                    clp('turning graphics off')
                    graphics_on = False
                    CA()
        else:#except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            clp('Exception!','`wrb',exc_type, file_name, exc_tb.tb_lineno)   






        f = freq_timer.freq(do_print=False)
        if is_number(f):
            clp( 'Frequency =', int(np.round(f*Nets[n]['P']['batch_size'])), 'Hz, run time =',format_seconds(run_timer.time()))




def Main6_Output_Object(net_str='pro2pros'):

    D = {}

    import torch
    import torch.nn as nn
    import torch.nn.parallel
    import torch.backends.cudnn as cudnn
    import torch.optim as optim
    import torch.utils.data
    import torchvision.datasets as dset
    import torchvision.transforms as transforms
    import torchvision.utils as vutils
    import torch.nn.utils as nnutils

    from .discriminator1 import Discriminator,weights_init



    if 'type' not in list(Arguments.keys()):
        clp('   FROM SYS_STR   ','`ybb',p=1)
        Nets = {
            'N0':Net_Main(M=M,sys_str=Net_strs[net_str].replace('\n',' ').replace('\t',' ')),
        }
    else:
        clp('   FROM COMMMAND LINE   ','`ybb',p=1)
        Nets = {
            'N0':Net_Main(M=M,Arguments_=Arguments),
        }

    n = 'N0'

    Data = networks_net.make_batch( Nets[n]['get_data_function'], Nets[n]['P'], Nets[n]['P']['batch_size'] )
    #cg('Data',shape(Data['input']),shape(Data['target']))

    DISCRIMINATOR = Discriminator(nc=shape(Data['target'])[1]).cuda()
    DISCRIMINATOR.apply(weights_init)
    criterion = nn.BCELoss()
    optimizerD = optim.Adam(DISCRIMINATOR.parameters(), lr=0.01, betas=(0.5, 0.999))



    run_timer = Timer()
    freq_timer = Timer(30)

    Abort = Toggler()

    wait_timer = Timer(5)

    minute_timer = Timer(60)



    def _function_output(in_imgs):

        if len(in_imgs) > 0:
            in_array = in_imgs[0]
            if len(in_imgs) > 1:
                for i in range(1,len(in_imgs)):
                    in_array = np.concatenate((in_array,in_imgs[i]),axis=2)
            in_array = na([in_array.transpose(2,1,0)])

        """
        M['load']()
        if Abort['test'](M['Q']['runtime_parameters']['abort']):
            return False#
        """

        if minute_timer.check():
            minute_timer.reset()
            Nets['N0']['P']['clip'] = float(Nets['N0']['P']['clip'])
            a = Nets['N0']['P']['clip']
            Nets['N0']['P']['clip'] *= 0.98
            clp('clip',Nets['N0']['P']['clip'],int(run_timer.time()),"`yb")

        
        GENERATOR = Nets[n]['N']
        Nets[n]['P']['original_Fire3_scaling'] = True

        """
        for k in list(M['Q']['runtime_parameters'].keys()):

            Nets[n]['P']['runtime_parameters'][k] = M['Q']['runtime_parameters'][k]
        """

        Data = networks_net.make_batch( Nets[n]['get_data_function'], Nets[n]['P'], Nets[n]['P']['batch_size'] )

        if len(in_imgs) > 0:
            Data['input'] = in_array

        GENERATOR.forward_no_loss(Data) 



        Nets[n]['graphics_function'](Nets[n]['N'],M,Nets[n]['P']) # graphics can cause an error with remote login
 
        fake = GENERATOR.extract('output')
        imgs = []
        for i in range(0,shape(Data['target'])[1],3):
            imgs.append(z55(fake[i:i+3,:,:].transpose(2,1,0)))
        return imgs

    D['output'] = _function_output

    return D



do_example = False
if do_example:


    from kzpy3.Learn.main import Main6_Output_Object
    M = Main6_Output_Object('pro2pros')
    a=z55(rnd((94,168,3)))
    b = 0*a; b[:,:,0] = 1
    in_imgs = [a,b]
    imgs = M['output'](in_imgs)

    imgs = M['output']([])
    c = imgs[1]
    a = c.astype(float)
    a -= 0.
    n = 25
    a[a<0] = n
    aa = z55(a);mi(aa,'aaa')
    imgs = M['output']([aa,b])







Mains = {
    6: main6,
}
        







if __name__ == '__main__':
    Defaults = {
        ('main','blank'):int,
        ('net_str','blank'):str,
        ('save_output_2','blank'): bool,
        ('batch_size','blank') :int,
        ('save_timer_time','blank'): int,
        ('LR','blank') : float,
        ('runs','blank') : str,
        ('manual_input0','blank') :int,
        ('GPU','blank') :int,
        ('resume','blank'):bool,
        ('graphics_timer_time','blank'):int,
        ('backwards','blank'):bool,
        ('resume','blank'):bool,
        ('single_run','blank'):str,
        ('save_figures2','blank'):str,
    }
    Arguments = get_Arguments(Defaults)
    if Arguments['main'] == 6:
        #kprint(Arguments)
        clp('*** main6() ***',p=2)
        if 'net_str' not in Arguments:
            Arguments['net_str'] = ''
        Mains[6]()












#EOF
