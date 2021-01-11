
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
A['in'] = ' '.join(A['in'])
A['out'] = ' '.join(A['out'])

exec(A_to_vars_exec_str)

#,a

from striprtf.striprtf import rtf_to_text 

f = '/Users/karlzipser/Desktop/novel0.rtf'
f = in_#opjD('eg.rtf')
#f = select_file(opjD())[0]

t = file_to_text(f)

u = t.replace('\i ','<italics>')
v = u.replace('\i0 ','</italics>')
w = rtf_to_text(v)
x = re.sub("^(\\n)+",'',w)
y = re.sub("(\\n|\\x95|\s)+$",'',x)
z = re.sub("(\\t)+",'\\t',y)
if num_tabs_ == 2:
	z = re.sub("\\t",'\\t\\t',z)
z = re.sub("^[0-9].*?\\n+",'',z)
z = re.sub("^.*2008.*?\\n+",'',z)
z = z.replace("\n","\\\n")

z1 = z.replace('<italics>',"\n\\f1\\i ")
z2 = z1.replace('</italics>',"\n\\f0\\i0 ")

text = z2

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

text = "\\fs"+str(big_font_)+" "+text[0]+"\n\\fs"+str(small_font_)+"\n" + text[1:]
o = header + text + footer
text_to_file(out_,o)

#,b

#EOF
