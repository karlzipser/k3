

def lines_from_hist_file(path):
	r = r'(^\s*\d+\s+)([\w\./\-].*)'
	q = []
	h = txt_file_to_list_of_strings(path)
	for l in h:
		m = re.match(r,l)
		if m:
			g = m.groups()
			#print(qtd(m[2]))
			if len(g) > 1:
				s = m[2]
				while s[-1] == ' ' and len(s) > 0:

					s = s[:-1]
					#cg(qtd(s))
				q.append(s)
		else:
			cr(l,r=1)
	return q

q = lines_from_hist_file( opjD('hist.txt') )



D = {}
oD = dict_access(D,'D/')
c = []
for b in q:
	print(b)
	n = 0
	for d in b.split(' '):
		#cr(d)
		if d == '' or str_is_int(d):
			n += 1
			#print(n)
	e = ' '.join( b.split(' ')[n-1:] )
	#Ecy(e)
	c.append(e)



for a in c:
	if len(a) > 0:
		try:
			#cy(a)
			path = '/'.join( a.split(' ') )
			#cb(a,path)
			if path[0] == '/':
				path = path[1:]
			if path[-1] != '/':
				path = path + '/'
			oD( path, e=a )
			#cg(path)
		except KeyboardInterrupt:
		    cr('*** KeyboardInterrupt ***')
		    sys.exit()
		except Exception as e:
		    exc_type, exc_obj, exc_tb = sys.exc_info()
		    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		    print('Exception!')
		    print(d2s(exc_type,file_name,exc_tb.tb_lineno))   
#oD(z=1);



#EOF
