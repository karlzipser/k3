

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
			cr(l,r=1)
	return q

histfile = opjD('hist.txt')
#os_system('rm',histfile)
#os_system('history >',histfile)
q = lines_from_hist_file(histfile)

D = {}
oD = dict_access(D,'D')

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




#EOF
