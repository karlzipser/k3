#!/usr/bin/env python3



def et():
	print(
		"""

import Menu.main
Q = Menu.main.start_Dic(
    dic_project_path=pname(opjh(__file__)),
    Dics={},
    Arguments={
        'menu':False,
        'read_only':False,
    }
)
Q['load']()
T = Q['Q']
import k3.drafts.Grapher.defaults as defaults
P = defaults.P





except KeyboardInterrupt:
    cr('*** KeyboardInterrupt ***')
    sys.exit()
except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	CS_('Exception!',emphasis=True)
	CS_(d2s(exc_type,file_name,exc_tb.tb_lineno),emphasis=False)		

		"""
		)

if __name__ == '__main__':
	et()


#EOF
