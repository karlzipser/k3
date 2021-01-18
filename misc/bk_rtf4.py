
#,bkr.a
"""
python3 k3/misc/bk_rtf4.py\
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
        'number_font':60,
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

#f = '/Users/karlzipser/Desktop/novel0.rtf'
#in_ = opjD('out.rtf')#in_#opjD('eg.rtf')
#out_ = opjD('out2.rtf')
#big_font_ = 60
#small_font_ = 38
#f = select_file(opjD())[0]

header = """{\\rtf1\\ansi\\ansicpg1252\\cocoartf2576
\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fnil\\fcharset0 Georgia;\\f1\\fnil\\fcharset0 Georgia-Italic;}
{\\colortbl;\\red255\\green255\\blue255;}
{\\*\\expandedcolortbl;;}
\\margl1440\\margr1440\\vieww11300\\viewh13520\\viewkind0
\\hyphauto1\\hyphfactor90
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qj\\partightenfactor0
\\f0\\fs38 \\cf0"""# \\\n"""

header = """{\\rtf1\\ansi\\ansicpg1252\\cocoartf2577
\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fnil\\fcharset0 Georgia;\\f1\\fnil\\fcharset0 Georgia-Italic;}
{\\colortbl;\\red255\\green255\\blue255;}
{\\*\\expandedcolortbl;;}
\\margl1440\\margr1440\\vieww11300\\viewh13520\\viewkind0
\\hyphauto1\\hyphfactor90
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0

\\f0\\fs60 \\cf0 <number>
\\fs38 \\
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qj\\partightenfactor0
"""

footer = """\n\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0
\\cf0    
\\'95 \\'95 \\'95\\
\\
}"""



t = file_to_text(in_)
if '<double>' in t:
    double = True
    t = t.replace('<double>','')
else:
    double = False
t = t.replace('\\i0 ','</italics>')
t = t.replace('\\i ','<italics>')
t = t.replace('\\i0','</italics>')
t = t.replace('\\i','<italics>')

t = t.replace("\\'94",'"')
t = t.replace("\\'93",'"')
t = t.replace("\\'92","'")
t = t.replace("\\'91","'")
t = re.sub("(\t)+",'',t)

t = rtf_to_text(t)
marker = '__'
s = re.match("^[\s\S]*__",t)
#s = re.match("[\s\S]*__[\s\S]*__",t)
if s is not None:
    s = s.span()
    intro = t[s[0]:s[1]]
    t = t[s[1]:]
else:
    intro = ''

t = re.sub("^([\s\t\n]*)",'',t)

t = re.sub("\n(\t|\\n|\.|\x95|\s)+$",'',t)

if True:
    s = re.match("^[\"|\']?[A-Z]",t)
    if s is not None:
        first_letter_index = s.span()[-1] - 1
    else:
        cE("first_letter_index is None")
        assert False #first_letter_index = 0
    if first_letter_index > 0:
        t0 = t[:first_letter_index]
        t = t[first_letter_index:]
    else:
        t0 = ''
    t = t0 + "\\fs"+str(big_font_)+" "+t[0]+"<n>\\fs"+str(small_font_)+"<n>" + t[1:]

if double:
    t = re.sub("\n\n\n",'<nnn>',t)
    t = re.sub("\n\n",'<nn>',t)
    t = re.sub('<nn>','\n',t)
    t = re.sub('<nnn>','\n\n',t)
t = re.sub("\n\n[\n]+",'\n\n',t)
t = re.sub("\n\n",'<section>',t)

sections = t.split('<section>')

for i in rlen(sections):
    sections[i] = sections[i].split('\n')

#number = "\n\\fs"+str(big_font_)+" "+str(number_)+"\n\\fs"+str(small_font_)+"\\\n"
t = header.replace('<number>',str(number_))# + number
t += '\n' + intro.replace('\n','\\\n').replace("__","__\\\n\\\n")

for paragraphs in sections:
    for i in rlen(paragraphs):
        p = paragraphs[i]
        if i > 0:
            p = '\t' + p
        t += p + '\\\n'
    t += '\\\n' 
t += footer

t = t.replace('<n>','\n')

t = t.replace('<italics>',"\n\\f1\\i\n")
t = t.replace('</italics>',"\n\\f0\\i0\n")

t = t.replace('__',"\\fs"+str(small_font_//4)+" __\n\\fs"+str(small_font_)+"\n")

if num_tabs_ == 2:
    t = re.sub("\t",'\t\t',t)

if False:
    for a in w.split('\n'):
        print(a,'\n')





    x = re.sub("^(\\n)+",'',w)
    y = re.sub("(\\n|\\x95|\s)+$",'',x)
    #z = re.sub("(\\t)+",'\\t',y)




    if num_tabs_ == 2:
    	z = re.sub("\\t",'\\t\\t',z)
    cy(z)



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

text_to_file(out_,t)

#,b

#EOF
