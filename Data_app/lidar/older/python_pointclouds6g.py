#!/usr/bin/env python

from k3.vis3 import *
import sensor_msgs
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import rospy

TX1 = False
if username == 'nvidia':
    TX1 = True
    cs("Using TX1")

Output = {}

A = {}
A['use_images'] = 0
A['time'] = 10
for a in Arguments:
    A[a] = Arguments[a]


waiting = Timer(1)
freq_timer = Timer(5);
timer = Timer(A['time'])

calls = 0
calls_prev = 0

if TX1:
    #field_names = ['t','reflectivity']
    field_names = ['reflectivity','intensity']
    width = 1024/2
else:
    field_names = ['y','intensity']
    width = 1024

height = 16
width_times_height = width * height


for f in field_names:
    A[f] = zeros((width,height))


######################################
#
Y = {}
mx = 2*np.pi*1000.0 #6290
extra = 40
for d in range(0,int(mx+extra)):
    v = int( width*d / (1.0*mx) )
    if v > (width-1):
        v = (width-1)
    Y[d] = v

j = 0
for i in range(sorted(Y.keys())[-1]):
    if i in Y:
        j = Y[i]
    Y[i] = j

Y[np.nan] = 0
#
######################################



def points__callback(msg):
    global calls
    #calls += 1
    
    ctr = 0
    ctr2 = 0
    ctr3 = 0
    
    ary0 = A[field_names[0]]
    ary1 = A[field_names[1]]
    
    for point in pc2.read_points(msg,skip_nans=False,field_names=field_names):

        if ctr2 == 1:
            if ctr3 >= height-1:
                ctr3 = 0
                ctr += 1
            else:
                ctr3 += 1

            if ctr >= width:
                if ctr3 >= height-1:
                    break
                ctr = 0
            ary0[ctr,ctr3] = point[0]  
            ary1[ctr,ctr3] = point[1]
        ctr2 += 1
        if ctr2 >= 4:
            ctr2 = 0

    calls += 1

rospy.init_node('receive_pointclouds')
rospy.Subscriber('/os1_node/points', PointCloud2, points__callback)


def process_calback_data():

    if TX1:
        b = A['reflectivity']
        y = (b[:,8]).astype(int)
        b2 = A['intensity']
    else:
        b = A['y']
        y = (b[:,8]*1000).astype(int)
        b2 = A['intensity']

    indicies = [Y[v] for v in y]

    #d = 0*b
    #d[indicies,:] = b

    d2 = b2*0
    d2[indicies,:] = b2

    for i in range(1,len(d2)):

        #if d[i,0] == 0:
        #    d[i,:] = d[i-1,:]

        if d2[i,0] == 0:
            d2[i,:] = d2[i-1,:]

    if TX1:
        e = cv2.resize(d2[68:448,:],(94,168))
    else:
        e = cv2.resize(d2,(64,1024))


    return e





print_Arguments()

while calls < 1:
    waiting.message('waiting for data...')
    time.sleep(0.01)

timer.reset()

while not timer.check():

    try:
        calls_ = calls

        if calls_ > calls_prev:

            freq_timer.freq()
    
            Output['e'] = process_calback_data()

            if A['use_images']:
                #figure('d');clf();plot(d);xlim(0,(width-1))
                #figure('d2');clf();plot(d2);xlim(0,(width-1));spause()#;raw_enter()
                mi(Output['e'].transpose(1,0));spause()#;raw_enter()

        calls_prev = calls_

    except:
        cs('exception',calls)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        CS_('Exception!',emphasis=True)
        CS_(d2s(exc_type,file_name,exc_tb.tb_lineno),emphasis=False)




"""
tegra-ubuntu> ~ $ nc 192.168.1.251 7501

get_config_txt

{"auto_start_flag": 1, "tcp_port": 7501, "udp_ip": "192.168.1.103", "udp_port_lidar": 7502, "udp_port_imu": 7503, "timestamp_mode": "TIME_FROM_INTERNAL_OSC", "pps_out_mode": "OUTPUT_PPS_OFF", "pps_out_polarity": "ACTIVE_HIGH", "pps_rate": 1, "pps_angle": 360, "pps_pulse_width": 10, "pps_in_polarity": "ACTIVE_HIGH", "lidar_mode": "1024x10", "motor_phase_lock_enable": 0, "motor_phase_offset": 0, "motor_enable": 0, "pulse_mode": "STANDARD", "window_rejection_enable": 0}

set_config_param lidar_mode 512x10
set_config_param

reinitialize

reinitialize

get_config_txt

{"auto_start_flag": 1, "tcp_port": 7501, "udp_ip": "192.168.1.103", "udp_port_lidar": 7502, "udp_port_imu": 7503, "timestamp_mode": "TIME_FROM_INTERNAL_OSC", "pps_out_mode": "OUTPUT_PPS_OFF", "pps_out_polarity": "ACTIVE_HIGH", "pps_rate": 1, "pps_angle": 360, "pps_pulse_width": 10, "pps_in_polarity": "ACTIVE_HIGH", "lidar_mode": "512x10", "motor_phase_lock_enable": 0, "motor_phase_offset": 0, "motor_enable": 0, "pulse_mode": "STANDARD", "window_rejection_enable": 0}

"""

"""
        calls_ = calls

        if calls_ > calls_prev:

            freq_timer.freq()
            
            if TX1:
                b = A['reflectivity']
                y = (b[:,8]).astype(int)
                b2 = A['intensity']
            else:
                b = A['y']
                y = (b[:,8]*1000).astype(int)
                b2 = A['intensity']

            indicies = [Y[v] for v in y]

            #d = 0*b
            #d[indicies,:] = b

            d2 = b2*0
            d2[indicies,:] = b2
        
            for i in range(1,len(d2)):

                #if d[i,0] == 0:
                #    d[i,:] = d[i-1,:]

                if d2[i,0] == 0:
                    d2[i,:] = d2[i-1,:]

            if TX1:
                e = cv2.resize(d2[68:448,:],(94,168))
            else:
                e = cv2.resize(d2,(64,1024))
            if A['use_images']:
                #figure('d');clf();plot(d);xlim(0,(width-1))
                #figure('d2');clf();plot(d2);xlim(0,(width-1));spause()#;raw_enter()
                mi(e.transpose(1,0));spause()#;raw_enter()

            calls_prev = calls_
"""

#EOF
