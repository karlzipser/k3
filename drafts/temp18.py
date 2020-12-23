#set theFoldersToProcess to choose folder with prompt "Please select the folders containing images to process:" default location "/Users/karlzipser/iCloud_Links" with multiple selections allowed


def select_with_Finder(location,folder=True,multiple=True):
	if folder:
		what = 'theFolderToProcess'
		choose = 'to choose folder with prompt'
		prompt = 'Select folder'
	else:
		what = 'theDocument'
		choose = 'to choose file with prompt'
		prompt = 'Select file'
	if multiple:
		prompt += 's:'
		mstr = 'with multiple selections allowed'
	else:
		prompt += ':'
		mstr = ''

	s = d2s(
		'set',
		what,
		choose,
		qtd(prompt),
		'default location',
		qtd(location),
		mstr,
	)

	tempfile = get_temp_filename(opjb())

	os_system('osascript -e ' + "'"+s+"' > "+tempfile,e=1)

	txt = file_to_text(tempfile)

	os_system('rm',tempfile,e=1)
	
	l0 = txt.split('alias')
	l1 = []
	for l in l0:
		l2 = l.split(':')
		l3 = []
		for m in l2:
			if m == '':
				continue
			if m[0] == ' ':
				if len(m) > 1:
					l3.append(m[1:])
					continue
			if m[0] == ',':
				continue
			if len(m) > 1 and m[-2:] == ', ':
				m = m[:-2]
			l3.append(m)
		if len(l3) > 0:
			l3 = ['/Volumes'] + l3
			l1.append(opj(*l3))
	return l1

location = "/Users/karlzipser/iCloud_Links"
l = select_with_Finder(location,multiple=True)
for m in l:
	os_system('open',qtd(m),e=1)
