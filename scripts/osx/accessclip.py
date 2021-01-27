#!/usr/bin/env python3

from k3.utils import *


A = get_Arguments(
	{
		'dst' : opjD('_clipboards.txt'),
		'delimiter' : '\n<====>\n',
		'n' : 20,
    },
    verbose=True,
    file=__file__,
)
exec(A_to_vars_exec_str)




try:
	while True:

		try:
			clipboards = file_to_text(dst_).split(delimiter_)
		except:
			clipboards = []
		if None in clipboards:
			clipboards.remove(None)
		if '' in clipboards:
			clipboards.remove('')

		clear_screen()

		for i in rlen(clipboards):
			c = clipboards[i]
			c = c.replace('\n',' ')
			c = c.replace('\t',' ')
			if len(c) > 60:
				c = c[:60] + '...'

			clp(str(i)+')','`w-b',c,'`y')
			
		j = input_int_in_range(0,len(clipboards),'choice > ')
		if j is not None:
			setClipboardData(clipboards[j])
			#time.sleep(1)
	
except KeyboardInterrupt:
    cw('\n\n*** done ***\n')
    sys.exit()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    cEd2s(exc_type,file_name,exc_tb.tb_lineno) 
#EOF


