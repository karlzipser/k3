#!/usr/bin/env python3

from k3.utils import *

Arguments = get_Arguments({'x':0,'m':9999})

save_dir = opjh('.'+fnamene(__file__))

os.system('mkdir -p ' + save_dir)

try:
	save_file = opj(save_dir,fnamene(__file__)+'.pkl')
	mtime = os.path.getmtime(save_file)
	timestamped_save_file = save_file.replace('.pkl','.'+str(int(mtime)))+'.pkl'
	os.system(d2s('cp',save_file,timestamped_save_file))
	lst = lo(save_file)
	just_text = []
	for l in lst:
		just_text.append(l[1])
		just_text.append(l[0])
		just_text.append('___\n')
	list_of_strings_to_txt_file(timestamped_save_file.replace('.pkl','.txt'),just_text)
except:
	lst = []

use_prefix_and_suffix = k_in_D('x',Arguments)

prefix = "Hi "
suffix = "! You seem like a fun and interesting person. It would be fascinating to get to know you. I'd love to hear more about your interests and passions."

E = {
	'Command':None,
	'noisy':False,
	'num_chars':100,
	'lst':lst,
	#'quit':False,
}

#istr =  cf('--> ','`gb-')


def clipthread():

	#()
	timer = Timer(Arguments['m']*60)
	while True:

		if timer.check():
			E['Command'] = 'quit'

		if E['Command'] == 'quit':
			cg('quitting clipthread()')

			return 0


		c = getClipboardData()

		if use_prefix_and_suffix and prefix not in c and suffix not in c:
			c = prefix + c + suffix
			setClipboardData(c)

		found = False
		for l in E['lst']:
			if c == l[0]:
				found = True

		if found:
			E['thread_sleeping'] = True
			time.sleep(0.2)
		else:
			E['thread_sleeping'] = False

			s = time_str('Pretty2')
			E['lst'].append( [c,s] )

			print_lst()

			so(E['lst'],save_file,noisy=E['noisy'])
			E['noisy'] = False

		


def print_lst():
	rows,cols = get_terminal_size()
	clear_screen()
	for i in rlen(E['lst']):
		m = min(len(E['lst'][i][0]), cols-10) #E['num_chars'])
		a = E['lst'][i][0][:m]
		b = a.split('\n')
		c = []
		for d in b:
			if len(d) > 0:
				c.append(d)
		if m < len(E['lst'][i][0]):
			dots = '...'
		else:
			dots = ''
		clp(str(i)+')','`---','\n'.join(c)+dots, '`---') #'`wbb')
		


threading.Thread(target=clipthread).start()

while True:

	try:
		while True:
			time.sleep(1)
			
			if E['Command'] == 'quit':
				sys.exit()

	except KeyboardInterrupt:
	    print('*** KeyboardInterrupt ***')
	    E['Command'] = 'quit'
	    time.sleep(1)
	    sys.exit()
	except Exception as e:
	    exc_type, exc_obj, exc_tb = sys.exc_info()
	    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	    cEd2s(exc_type,file_name,exc_tb.tb_lineno) 
#EOF

