
    if False:
        fs = sggo('/Volumes/Untitled/validation_runs/*')
        fs += sggo('/Volumes/Tilden/Tilden/LCR/h5py/*')

        for f in fs:
            os_system("ln -s",f,opj('/Users/karlzipser/Desktop/Data/validate_/h5py',fname(f)))

        if False:
            args = ' '.join(sys.argv[1:])
            cm(args,r=1)
            if '--run_from_string True' in args:
                cmd_line.replace('--run_from_string True','')
                os_system(cmd_line,e=1,a=1,r=1)
            cm(cmd_line.replace('--','\n--'),r=1)

        
        from k3.utils.vis.other import *


        r = "direct_Tilden_LCR_15Jul17_12h29m14s_Mr_Yellow"
        #p = "/Volumes/osx-data/3D_points_in_image_multistep/direct_Tilden_LCR_12Jul17_09h41m48s_Mr_Yellow/20300_to_-1"
        p = opj("/Volumes/Tilden/Tilden/LCR/h5py",r,'original_timestamp_data.h5py')
        O = h5r(p)

        
        start = 12000
        stop = 19200
        fig = figure(1)
        h = 94/2
        hs = []
        for i in range(start,stop,10):
            print(i)
            g = O['left_image']['vals'][i]
            clf()
            mi(g,1)
            plot([0,168],[h,h],'r')
            Cdat = Click_Data(FIG=fig)
            xy_list = Cdat['CLICK'](NUM_PTS=1)
            h = xy_list[0][1]
            hs.append([i,h])
            spause()
            time.sleep(0.2)