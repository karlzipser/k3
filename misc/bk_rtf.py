
#,a

f = '/Users/karlzipser/Desktop/novel_form0.out.rtf'

text_versions = [ file_to_text(f) ]


rules = (
    ( '<T>',        '\\t'),
    ( '<N>',        '\\n'),
    ( '<BS>',        "\\\\" ),
    ( '<CR>',       "<BS><N>" ),
    ( '<SECTION>',  "<CR>[' '|(<T>)|/.|<CR>]*<CR>" ),
)


for r in rules:
    replacement_,pattern_ = r[0],r[1]
    x = re.sub(pattern_,replacement_,text_versions[-1])
    text_versions.append(x)


big_ = 50
regular_ = 38
fl = d2n("(<BS>fs",big_,"[' ']+([A-Z])['<N>']*[' ']*<BS>fs",regular_,"['<N>']*)[' ']*")
fc = re.findall(fl,text_versions[-1])
assert len(fc) < 2
if len(fc):
    #u = re.findall(fc[0,text_versions[-1]) 
    #q = re.sub(fl,fc[0],text_versions[-1])
    q = re.sub(fc[0][0],fc[0][1],text_versions[-1])
    text_versions.append(q)


num_tabs_ = 2

def strip_paragraph_start(p):
    r = "^(<[a-z|A-Z|0-9]+>[' ']*)+"
    return re.sub(r,'',p)


sections = text_versions[-1].split('<SECTION>')
assert '{' in sections[0]
assert '}' in sections[-1]
for i in range(1,len(sections)-1):
    if "<BS>'95 <BS>'95 <BS>'95" in sections[i]:
        #cb(sections[i],r=False)
        sections[i] = ['<N>']
        continue
    s = sections[i]

    assert '{' not in s
    assert '}' not in s

    paragraphs = s.split('<CR>')

    for j in range(0,len(paragraphs)):
        p = paragraphs[j]
        #cg(p,r=True)
        p = strip_paragraph_start(p)
        #cy(p,r=True)
        if i == 1 and j == 0:
            #cm(p,p[0])
            if True:
                a = p[0]
                p = "\\fs50 "+a+"\n\\fs38\n"+p[1:]
                #print(p)
                paragraphs[j] = p
                #cr(p)

        if j > 0:
            p = num_tabs_*'<T>' + p

        paragraphs[j] = p

    sections[i] = paragraphs

l = [sections[0],'\\\n\\\n']
for i in range(1,len(sections)-1):
    for p in sections[i]:
        l.append(p+'\\\n')
    l.append('\\\n')


l.append(
    """\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\li722\\fi-16\\ri-738\\pardirnatural\\qc\\partightenfactor0
\\cf0    
\\'95 \\'95 \\'95\\
\\
""")

l.append(sections[-1])

o = '\n\n'.join(l)
o = o.replace('<T>','\t')
o = o.replace('<N>','\n')
o = o.replace('<BS>','\\')

ff = f.replace('.rtf','.out.rtf')

text_to_file(ff,o)
cy('wrote',ff)
#,b




"""
if j == 0 and p.startswith('<T>'):

    cr('Warning, starts with <T>')

elif j == 0 and not p.startswith('<T>'):
    cg('Ok')

elif not p.startswith('<T>'):
    if p[0] == ' ':
        cr('warning, starts with a space')
    cr(j,'warning, does NOT start with <T>, adding')
    p = '<T>' + p

elif p.startswith('<T>'):
    cg('ok')
"""

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

