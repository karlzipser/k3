#set theFoldersToProcess to choose folder with prompt "Please select the folders containing images to process:" default location "/Users/karlzipser/iCloud_Links" with multiple selections allowed


def _select_with_Finder(location,folder=True,multiple=True):
	if not os.path.isdir(location):
		return None
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
l = _select_with_Finder(location,multiple=True)
for m in l:
	os_system('open',qtd(m),e=1)


def select_file(path=opjh()):
	return _select_with_Finder(path,folder=False,multiple=False)

def select_files(path=opjh()):
	return _select_with_Finder(path,folder=False,multiple=True)

def select_folder(path=opjh()):
	return _select_with_Finder(path,folder=True,multiple=False)

def select_folders(path=opjh()):
	return _select_with_Finder(path,folder=True,multiple=True)





set theRichTextFile to quoted form of "/Users/karlzipser/Desktop/a.rtf"
set theCharacterCount to do shell script "textutil -stdout -convert txt " & theRichTextFile & " | LANG=en_US.UTF-8 wc -m | sed 's/ //g'"

osascript('set theRichTextFile to quoted form of "/Users/karlzipser/Desktop/a.rtf"')
set theCharacterCount to do shell script "textutil -stdout -convert txt " & theRichTextFile & " | LANG=en_US.UTF-8 wc -m | sed 's/ //g'"


s = """
set theRichTextFile to quoted form of "/Users/karlzipser/Desktop/a.rtf"
set theCharacterCount to do shell script "textutil -stdout -convert txt " & theRichTextFile & " | LANG=en_US.UTF-8 wc -m | sed 's/ //g'"
"""

def osa(script):
	assert using_platform() == 'osx'
	script_file,output_file = '',''
	while script_file == output_file:
		script_file = get_temp_filename()
		output_file = get_temp_filename()
		print(script_file,output_file)
	text_to_file(script_file,script)
	os_system('osascript',script,'>',output_file)
	output = file_to_text(output_file)
	os_system('rm',output_file)
	os_system('rm',script_file)
	return output

print(osa(s))


#,a
from striprtf.striprtf import rtf_to_text 
p = '/Users/karlzipser/Desktop/_2008 one -- Editing version 12-27-2020'  
rs = sggo(p,'*.rtf')
c = 0
d = []
for r in rs:
	if fname(r)[0] == '_':
		continue
	print(fnamene(r))
	a = file_to_text(r)
	b = rtf_to_text(a)
	c += sum([i.strip(string.punctuation).isalpha() for i in b.split()])
	d.append(b)
print(c,'words total')
text_to_file(opjD('joined.txt'),'\n\n\n...\n'.join(d))
#,b

"""
cb -s --val1 -i 0

set msg to "Input three letters for each of first letter, second letter, and third letter. Separate your responses by a comma (e.g. aaa,bbb,ccc)"
set delimAnswer to text returned of (display dialog msg default answer "--aaa --bbbb --cccc")

"""

#EOF

