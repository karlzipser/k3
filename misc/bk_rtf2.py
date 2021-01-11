
#,a
clear_screen()
f = '/Users/karlzipser/Desktop/novel_form_not.rtf'
#f = select_file(opjD())[0]

t = file_to_text(f)
u = t.replace('\n','<=N=>')
uu = re.sub('(\\\\f[0-9]+.+?<=N=>)','',u)
v = re.sub('^.+?<=N=><=N=>','',uu)
w = re.sub('\.\\\\(\\\\*<=N=>)+(\\\\pard.+)*\}','.',v)
print(w)

T = {
    'text': [w],

    'header':   ["""{\\rtf1\\ansi\\ansicpg1252\\cocoartf2576
\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fnil\\fcharset0 Georgia;\\f1\\fnil\\fcharset0 Georgia-Italic;}
{\\colortbl;\\red255\\green255\\blue255;}
{\\*\\expandedcolortbl;;}
\\margl1440\\margr1440\\vieww11300\\viewh13520\\viewkind0
\\hyphauto1\\hyphfactor90
\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qj\\partightenfactor0
\\f0\\fs38 \\cf0"""],

    'footer':   ["""\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0
\\cf0    
\\'95 \\'95 \\'95\\
\\
}"""],
}

rules = (
    ( '<=T=>',        '\\t'),
    #( '<=N=>',        '\\n'),
    ( '<=BS=>',        "\\\\" ),
    ( '<=CR=>',       "<=BS=><=N=>" ),
    ( '<=SECTION=>',  "<=CR=>[' '|(<=T=>)|/.|<=CR=>]*<=CR=>" ),
)


for r in rules:    
    replacement_,pattern_ = r[0],r[1]
    for k in T:
        x = re.sub(pattern_,replacement_,T[k][-1])
        T[k].append(x)

if True:
    big_ = 50
    regular_ = 38
    fl = d2n("(<=BS=>fs",big_,"[' ']+([A-Z])['<=N=>']*[' ']*<=BS=>fs",regular_,"['<=N=>']*)[' ']*")
    fc = re.findall(fl,T['text'][-1])
    assert len(fc) < 2
    if len(fc):
        q = re.sub(fc[0][0],fc[0][1],T['text'][-1])
        T['text'].append(q)


num_tabs_ = 2

def strip_paragraph_start(p):
    r = "^(<=[a-z|A-Z|0-9]+=>[' ']*)+"
    return re.sub(r,'',p)



sections = T['text'][-1].split('<=SECTION=>')


for i in range(0,len(sections)):
    
    s = sections[i]

    paragraphs = s.split('<=CR=>')

    for j in range(0,len(paragraphs)):
        p = paragraphs[j]
        #cg(p,r=True)
        p = strip_paragraph_start(p)
        #cw(p,r=True)
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

l = [ T['header'][-1] ]
for i in range(0,len(sections)):
    for p in sections[i]:
        l.append(p+'\\\n')
    l.append('\\\n')



l.append(T['footer'][-1])

o = '\n\n'.join(l)
o = o.replace('<=T=>','\t')
o = o.replace('<=N=>','\n')
o = o.replace('<=BS=>','\\')

ff = f.replace('.rtf','.out.rtf')

text_to_file(ff,o)
cy('wrote',ff)
#,b




