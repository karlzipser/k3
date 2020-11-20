from k3 import *
import k3.aps.Learn.networks.net as networks_net

def Net_Main(M=False,sys_str=False,Arguments_=False,P_Runs_saved=None):

    D = {}

    P = {
        'resume':1,
        'GPU':999,
        'momentum':0.001,
        'LR':0.01,
        'batch_size':64,
        'backwards':True,
        'losses_to_average':25,
        'save_timer_time':5*minutes,
        'runs':'train',
        'clip':1,
        'noise':0,
        'projection.noise':0,
        'input':False,
        'target':False,
        'display.output':[0,3],
        'display.input':[0,3],
        'display.target':[0,3],
        'batch_size':1,
        'losses_to_average':64,
        'input_offset':0,
        'target_offset':0,
        'Data_read_path':False,
        'Data_write_path':False,
        'runtime_parameters':{},
        'win_x':0,
        'win_y':0,
        'width':168,
        'height':94,
        'show_graphics':True,
    }

    if sys_str != False:
        Arguments_sys_str = parse_to_Arguments(sys_str)
    else:
        Arguments_sys_str = {}
        assert type(Arguments_) == dict

    for k in Arguments_sys_str:
        cg(k,'from Arguments_sys_str')
        P[k] = Arguments_sys_str[k]

    for k in Arguments_:
        cy(k,'from Arguments_')
        P[k] = Arguments_[k]

    kprint(P)

    for k in ['type','input','target']:
        if type(P[k]) == str:
            P[k] = [P[k]]

    assert P['type'][0] == 'Conv'
    from k3.aps.Learn.get_data.Conv import get_data_function
    import k3.aps.Learn.get_data.Conv as get_data_Conv
    if type(P_Runs_saved) != type(None):
        P['Runs'] = P_Runs_saved['Runs']
        P['good_list'] = P_Runs_saved['good_list']
        P['Run_coder'] = P_Runs_saved['Run_coder']
    else:
        get_data_Conv.setup(P)

    from k3.aps.Learn.graphics.Conv import graphics_function
    import k3.aps.Learn.networks.Conv as networks_Conv
    Network = networks_Conv.MyConv

    P['NETWORK_OUTPUT_FOLDER'] = opjD(
        'Networks',
        d2n(
            '.'.join(P['type'])
        ))

    Data = networks_net.make_batch( get_data_function, P, P['batch_size'] )
    Duplicates = {}
    for k in ['input','target']:
        Duplicates[k] = Data[k].copy()
    
    P['NUM_INPUT_CHANNELS'] = shape(Data['input'])[1]
    P['NUM_OUTPUTS'] = shape(Data['target'])[1]
    P['NUM_METADATA_CHANNELS'] = 10
    P['INPUT_WIDTH'] = shape(Data['input'])[2]
    P['INPUT_HEIGHT'] = shape(Data['input'])[3]

    N = Network(P)

    D['P'] = P
    D['N'] = N
    D['get_data_function'] = get_data_function
    D['graphics_function'] = graphics_function
    D['Duplicates'] = Duplicates

    return D


#EOF
