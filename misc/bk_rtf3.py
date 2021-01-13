
#,bkr.a
"""
python3 k3/misc/bk_rtf3.py\
    --in Desktop/eg.rtf\
    --out Desktop/out.rtf\
"""
#,bkr.b


from k3.utils import *

A = get_Arguments(
    {
    	'in':opjD('eg.rtf'),
    	'out':opjD('out.rtf'),
		'num_tabs':2,
		'big_font':50,
		'small_font':38,
    },
    file=__file__,
    r=False,
)
if type(A['in']) is list:
    A['in'] = ' '.join(A['in'])
if type(A['out']) is list:
    A['out'] = ' '.join(A['out'])

exec(A_to_vars_exec_str)

#,a

from striprtf.striprtf import rtf_to_text 

f = '/Users/karlzipser/Desktop/novel0.rtf'
f = in_#opjD('eg.rtf')
#f = select_file(opjD())[0]

header = """{\\rtf1\\ansi\\ansicpg1252\\cocoartf2576
\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fnil\\fcharset0 Georgia;\\f1\\fnil\\fcharset0 Georgia-Italic;}
{\\colortbl;\\red255\\green255\\blue255;}
{\\*\\expandedcolortbl;;}
\\margl1440\\margr1440\\vieww11300\\viewh13520\\viewkind0
\\hyphauto1\\hyphfactor90
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qj\\partightenfactor0
\\f0\\fs38 \\cf0 \\\n"""

footer = """\\\n\\\n\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0
\\cf0    
\\'95 \\'95 \\'95\\
\\
}"""

t = file_to_text(f)

u = t.replace('\i0 ','</italics>')
v = u.replace('\i','<italics>')

v = v.replace("\\'94",'\"')
v = v.replace("\\'93",'\"')
cm(v)
w = rtf_to_text(v)
cr(w)
x = re.sub("^(\\n)+",'',w)
y = re.sub("(\\n|\\x95|\s)+$",'',x)
#z = re.sub("(\\t)+",'\\t',y)
z = re.sub("(\\t)+",'',y)



if num_tabs_ == 2:
	z = re.sub("\\t",'\\t\\t',z)
cy(z)

z = re.sub("^.*2008.*?\\n+",'',z)
z = re.sub("^[\\|\n|\s|\t]*[0-9].*?\\n+",'',z)

z = z.replace("\n","\\\n")
cm(z)
#s = re.match("^([\n|\s|\t]*([<italics>].+?[</italics>])+)*[\n|\s|\t]*\"?",t).span()
#s = re.match("^[<italics>].+?[</italics>]",t).span()
#print(s)
#za = z[s[0]:s[1]]
#zb = z[s[1]:]
#cr(za)
#cg(zb)
if z[0].isalpha():
    text = "\\fs"+str(big_font_)+" "+z[0]+"\n\\fs"+str(small_font_)+"\n" + z[1:]
else:
    text = z
text = text.replace('<italics>',"\n\\f1\\i ")
text = text.replace('</italics>',"\n\\f0\\i0 ")




#text = "\\fs"+str(big_font_)+" "+text[0]+"\n\\fs"+str(small_font_)+"\n" + text[1:]
o = header + text + footer
text_to_file(out_,o)

#,b

#EOF
