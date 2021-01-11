
#,a
clear_screen()
f = '/Users/karlzipser/Desktop/novel_form_not.out.rtf'
#f = select_file(opjD())[0]

ending = """\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0
\\cf0    
\\'95 \\'95 \\'95\\
\\
"""

text_versions = [ file_to_text(f) ]
#.replace(ending,'')

rules = (
    ( '<=T=>',        '\\t'),
    ( '<=N=>',        '\\n'),
    ( '<=BS=>',        "\\\\" ),
    ( '<=CR=>',       "<=BS=><=N=>" ),
    ( '<=SECTION=>',  "<=CR=>[' '|(<=T=>)|/.|<=CR=>]*<=CR=>" ),
)


for r in rules:
    replacement_,pattern_ = r[0],r[1]
    x = re.sub(pattern_,replacement_,text_versions[-1])
    text_versions.append(x)
    #print('\n\n\n*** ',pattern_,'-->',replacement_,' ***\n\n',text_versions[-1])
    #raw_enter()

big_ = 50
regular_ = 38
fl = d2n("(<=BS=>fs",big_,"[' ']+([A-Z])['<=N=>']*[' ']*<=BS=>fs",regular_,"['<=N=>']*)[' ']*")
fc = re.findall(fl,text_versions[-1])
assert len(fc) < 2
if len(fc):
    q = re.sub(fc[0][0],fc[0][1],text_versions[-1])
    text_versions.append(q)



num_tabs_ = 2

def strip_paragraph_start(p):
    r = "^(<=[a-z|A-Z|0-9]+=>[' ']*)+"
    return re.sub(r,'',p)


sections = text_versions[-1].split('<=SECTION=>')


sections[0] = """{\\rtf1\\ansi\\ansicpg1252\\cocoartf2576
\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fnil\\fcharset0 Georgia;\\f1\\fnil\\fcharset0 Georgia-Italic;}
{\\colortbl;\\red255\\green255\\blue255;}
{\\*\\expandedcolortbl;;}
\\margl1440\\margr1440\\vieww11300\\viewh13520\\viewkind0
\\hyphauto1\\hyphfactor90
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qj\\partightenfactor0
\\f0\\fs38 \\cf0
"""

assert '{' in sections[0]
assert '}' in sections[-1]

for i in range(1,len(sections)-1):
    if False:#"<=BS=>'95 <=BS=>'95 <=BS=>'95" in sections[i]:
        sections[i] = ['<=N=>']
        continue
    s = sections[i]
    
    assert '{' not in s
    assert '}' not in s

    paragraphs = s.split('<=CR=>')

    for j in range(0,len(paragraphs)):
        p = paragraphs[j]
        cg(p,r=True)
        p = strip_paragraph_start(p)
        cw(p,r=True)
        if i == 1 and j == 0:
            if True:
                a = p[0]
                p = "\\fs50 "+a+"\n\\fs38\n"+p[1:]
                #print(p)
                paragraphs[j] = p
                #cr(p)

        if j > 0:
            p = num_tabs_*'<=T=>' + p

        paragraphs[j] = p

    sections[i] = paragraphs

l = [sections[0],'\\\n\\\n']
for i in range(1,len(sections)-1):
    for p in sections[i]:
        l.append(p+'\\\n')
    l.append('\\\n')


#l.append(ending)


l.append(sections[-1])

o = '\n\n'.join(l)
o = o.replace('<=T=>','\t')
o = o.replace('<=N=>','\n')
o = o.replace('<=BS=>','\\')

ff = f.replace('.rtf','.out.rtf')

text_to_file(ff,o)
cy('wrote',ff)
#,b






def pure_text(s):
    rs = [
        "<BS>[a-z0-9]+[' ']*",
        "<[A-Z0]+>",
        " [' ']+",
    ]
    for r in rs:
        s = re.sub(r,' ',s)
    if s[0] == ' ':
        s = s[1:]
    return s

#EOF

