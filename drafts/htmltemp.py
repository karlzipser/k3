from k3 import *
br = '<br>\n'
def lines_to_html_str(print_lines):
    if type(print_lines) == str:
        print_lines = print_lines.split('\n')
    assert type(print_lines) == list
    h = '\n \n'.join(print_lines).replace(' ','&nbsp').encode('ascii', 'xmlcharrefreplace').decode('utf8')
    replace_list = list(range(100))
    for i in rlen(replace_list):
        replace_list[i] = d2n('[',replace_list[i],'m')
    for s in replace_list:
        h = h.replace(s,'')
    return h
l2h = lines_to_html_str

def head_(s):
	a = """
<html>
<head>
<title>
		"""
	b = """
</title>
</head>
<body>
		"""
	return a + s + b


def img_(src,style):
	return d2n('\n<img src=',qtd(src),' style=',qtd(style),'>\n')


def href_(dst,s):
	return d2n('\n<a href=',qtd(dst),'>',s,'</a>\n')


def form_(s):
	return """\n<form action="" method="GET">\n""" + \
		s + " <input type='text' name='"+get_safe_name(s)+"''>\n" + \
		"</form>\n"


def end_():
	return "\n</body></html>\n\n"


#EOF

