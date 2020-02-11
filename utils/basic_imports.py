from __future__ import print_function
from __future__ import division

import_list = ['os','os.path','shutil','scipy','scipy.io','string','glob','time','sys','datetime','random','re',
    'subprocess','threading','serial','inspect','fnmatch','h5py','socket','getpass','numbers','math']#,'importlib']
import_from_list = [['FROM','pprint','pprint'],['FROM','termcolor','cprint']]
import_as_list = [['AS','numpy','np'],['AS','cPickle','pickle']]

for im in import_list + import_from_list + import_as_list:
    if type(im) == str:
        try:
            exec('import '+im)
        except:
            pass
            print('Failed to import '+im)
    else:
        assert(type(im)) == list
        if im[0] == 'FROM':
            try:
                exec('from '+im[1]+' import '+im[2])
                print("from "+im[1]+" imported "+im[2])
            except:
                pass
                print('Failed to from '+im[1]+' import '+im[2])
        else:
            assert(im[0] == 'AS')
            try:
                exec('import '+im[1]+' as '+im[2])
            except:
                pass
                print('Failed to import '+im[1]+' as '+im[2])

#EOF
