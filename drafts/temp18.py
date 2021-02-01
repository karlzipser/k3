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


#, a
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
    break


#,b
    c += sum([i.strip(string.punctuation).isalpha() for i in b.split()])
    d.append(b)
print(c,'words total')
text_to_file(opjD('joined.txt'),'\n\n\n...\n'.join(d))
#, b



#, a
from striprtf.striprtf import rtf_to_text 
p = '/Users/karlzipser/Desktop/_2008 one -- Editing version 12-27-2020'  
rs = sggo(p,'*.rtf')
bb = []
ctr = 0
for r in rs:
    if fname(r)[0] == '_':
        continue
    print(fnamene(r))
    a = file_to_text(r)
    b = rtf_to_text(a)
    bb.append(b)
b = '\n\n'.join(bb)
b = b.lower()
c = []
for d in b: 
    if d.isalpha(): 
        c.append(d) 
    else: 
        c.append(' ')
e=''.join(c)
f=e.split(' ')
g=remove_empty(f)
C = {}
for h in g:
    if h not in C:
        C[h] = 1
    else:
        C[h] += 1

gg = nltk.word_tokenize(e)
ggg = nltk.pos_tag(gg)

#, b


"""
cb -s --val1 -i 0

set msg to "Input three letters for each of first letter, second letter, and third letter. Separate your responses by a comma (e.g. aaa,bbb,ccc)"
set delimAnswer to text returned of (display dialog msg default answer "--aaa --bbbb --cccc")


echo $(python3 k3/scripts/osx/select_files.py)
a=$(python3 k3/scripts/osx/select_files.py)
mclip -m $a

"""

"""
# https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/

POS tag list:

CC  coordinating conjunction
CD  cardinal digit
DT  determiner
EX  existential there (like: "there is" ... think of it like "there exists")
FW  foreign word
IN  preposition/subordinating conjunction
JJ  adjective   'big'
JJR adjective, comparative  'bigger'
JJS adjective, superlative  'biggest'
LS  list marker 1)
MD  modal   could, will
NN  noun, singular 'desk'
NNS noun plural 'desks'
NNP proper noun, singular   'Harrison'
NNPS    proper noun, plural 'Americans'
PDT predeterminer   'all the kids'
POS possessive ending   parent\'s
PRP personal pronoun    I, he, she
PRP$    possessive pronoun  my, his, hers
RB  adverb  very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP  particle    give up
TO  to  go 'to' the store.
UH  interjection    errrrrrrrm
VB  verb, base form take
VBD verb, past tense    took
VBG verb, gerund/present participle taking
VBN verb, past participle   taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present  takes
WDT wh-determiner   which
WP  wh-pronoun  who, what
WP$ possessive wh-pronoun   whose
WRB wh-abverb   where, when
"""


#, a

import re

txt = "I like to <cello-sascha saschais 0.9> one </cello> often. I like to <cello-a b 0.9999> two </cello> often."
r = "(<cello(.*?)>(.+?)</cello>)"
x = re.findall(r,txt)
for i in range(3):
    try:
        y = x[i]
        print(i,qtd(y))
    except:
        break

#, b

#, a
txt = """
I like to <cello-sascha saschais 0.9> one </cello> often. I like to <cello-a b 0.9999> <quartet-a b 0.9999> two </cello> often."I like to  one </quartet> often. I like to <cello-a b 0.9999> two </cello> often."
"""

tags = ['cello','quartet']
tag_str = "(<TAG(.*?)>(.+?)</TAG>)"
R = {}
for t in tags:
    R[t] = tag_str.replace('TAG',t)


import re
for t in R:
    cg(t)
    pattern = re.compile(R[t])
    r = pattern.search(txt)
    if not r: print("(-1, -1)")
    while r:
        print(r)
        print("({0}, {1})".format(r.start(), r.end() - 1))
        r = pattern.search(txt,r.start() + 1)


#, b

#, a
"""
book = [
    chapters: [
     {
        summary:,
        rating:,
        sections: [
            {
                summary:,
                rating:,
                paragraphs [
                    {
                        tags:,
                        text:''
                    },
                    {
                        tags:,
                        text:''
                    },
                    {
                        tags:,
                        text:''
                    },
                ],
            },
            {
                summary:,
                rating:,
                paragraphs [
                    {
                        tags:,
                        text:''
                    },
                    {
                        tags:,
                        text:''
                    },
                    {
                        tags:,
                        text:''
                    },
                ],
            },
    },
]
"""





txt = "<section><cello abc def><quartet></love></cello>"

T = {
    'open' : "<([a-z|A-Z]+)(.*?)>",
    'close' : "</([a-z|A-Z]+)>",
}

for k in T:
    x = re.findall(T[k],txt)
    print(k,x)


#, b


#, a
txt = """He seemed to radiate like the sun, and Sacha was his earth, his most favored satellite. Sara seemed to feel eclipsed before her, as indeed Sacha stepped a bit in front of her. Sacha's glow was irrepressible and Sara found it impossible to feel that she had a place between them, it confused her and she felt uncomfortable. She saw how Thomas reacted to Sacha's charm, she felt she should be threatened, but their manner was so natural and beautiful that she couldn't help but feel charmed, it was more like seeing her son with a beautiful woman than feeling her boyfriend was being stolen from her. She felt a voyeuristic pleasure in seeing them. Sacha smiled and moved her arms and hands as she spoke, Thomas smiled and grinned and he was handsome. Sara thought, how beautiful that he can be so close to his student. She felt like she knew Sacha already for a long time, although they had just met. It was strange. Sacha seemed to radiate happiness and self confidence, the feeling made Sara feel happy too. Then Sacha turned to her and spoke to her and joined her into the conversation. She had such natural good manners, Sara couldn't help but be fond of her.\\"""
Then Sacha came back to her to ask her about playing the violin, what the secrets to good intonation are, and Sara shared what she knew how to explain in words, and tried not to say more than she really knew, for it was all to easy to let words form ideas that had little resemblance to what she actually did. It would be like asking an athlete how he runs. What could he explain?\\
A voice inside Sara told her that Sacha was a threat to her, but the voice seemed half-hearted, the words spoken with a smile, and she disregarded the warning. Sacha seemed genuinely interested in her, how could she be a rival? Sacha was asking if she could have some introductory lessons on the violin. Sara said again that the technique for the two instruments conflicted, and that it was necessary to choose.\\
"But how can I choose if I don't learn something about both instruments?"\\
Sara laughed at the inevitable logic of what she was saying. Sacha looked directly into her eyes when she spoke. She seemed to have a benevolent power over Sara, she only wanted to submit and be embraced by Sacha's charisma. Sacha had a genuine and deep interest in what Sara did, she was fascinated by ever detail, and Sara felt happy to be accomplished at something that Sacha found so important.\\
In the back of her mind, Sacha was aware of some practical problems. How was she going to get Thomas away from Sara this evening so that they could make love? She noticed that Thomas and Sara did not touch each other here in public.\\"""


r = "(.*?)(\\\\$)"

x = re.findall(r,txt)
print(x)


#, b



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
    pat,repl = r[1],r[0]
    #clp('\n\n',pat,'`--ub',repl,'`--ub')
    x = re.sub(pat,repl,text_versions[-1])
    text_versions.append(x)

fl = "<BS>fs50[' ']+([A-Z])[' ']*['<N>']*[' ']*<BS>fs38[' ']*"
fc = re.findall(fl,text_versions[-1])
assert len(fc) == 1
q = re.sub(fl,fc[0],text_versions[-1])
text_versions.append(q)



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

sections = text_versions[-1].split('<SECTION>')
assert '{' in sections[0]
assert '}' in sections[-1]
for i in range(1,len(sections)-1):
    if "<BS>'95 <BS>'95 <BS>'95" in sections[i]:
        cb(sections[i],r=False)
        sections[i] = ['<N>']
        continue
    s = sections[i]
    assert '{' not in s
    assert '}' not in s
    paragraphs = s.split('<CR>')
    for j in range(0,len(paragraphs)):
        p = paragraphs[j]
        if False:#i == 1 and j == 0:
            cg(p[0],'\n',p)
            a = p[0]
            p = "\\fs50 "+a+"\n\\fs38\n"+p[1:]
            print(p)
            paragraphs[j] = p
        clp('\nSection',i,'paragraph',j+1,'`--b')
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

            paragraphs[j] = p
    sections[i] = paragraphs


l = [sections[0],'\\\n\\\n']
for i in range(1,len(sections)-1):
    for p in sections[i]:
        l.append(p+'\\\n')
    l.append('\\\n\\\n')

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

for k in R:
    r = R[k]
    x = re.findall(r,txt)
    #print(x)
    for i in range(3):
        try:
            y = x[i]
            print(k,i,qtd(y))
        except:
            break

#, a

path  = opjD("a")#opjD("_2008 one -- Editing version 12-27-2020")
newp = opjD("a_new")
fs = sggo(path,'*.rtf')


os_system('mkdir -p',newp)

for f in fs:
    if fname(f)[0] != '_':
        if '40' in fname(f)[:2]:
            print(f)
            number = fnamene(f).split(' ')[0]
            g = number+'.rtf'
            os_system('python3 k3/misc/bk_rtf4.py --number',number,'--in',qtd(f),'--out',qtd(opj(newp,g)),e=1)
            #break

#, b
#, a

path  = opjD("A")#opjD("_2008 one -- Editing version 12-27-2020")
newp = opjD("A_new")
fs = sggo(path,'*.rtf')


os_system('mkdir -p',newp)

for f in fs:
    if fname(f)[0] != '_':
        if True:#'40' in fname(f)[:2]:
            print(f)
            number = fnamene(f).split(' ')[0]
            g = number+'.rtf'
            os_system('python3 k3/misc/bk_rtf4.py --number',number,'--in',qtd(f),'--out',qtd(opj(newp,g)),e=1)
            #break

#, b

if False:
    fs = sggo(opjD('a','*.rtf'))
    for f in fs:
        if '  ' in f:
            os_system('mv',qtd(f),qtd(f.replace('  ',' ')),a=1,e=1)

#,a
x = [37, 42, 47, 52]
y = [52, 36,  5,  0]
from scipy import interpolate
f = interpolate.interp1d(x, y)
xnew = np.arange(37, 52, 1./12.)
ynew = f(xnew)
plot(x, y, 'o', xnew, ynew, '-')
(1-float(q(45))/100.)
#,b

#EOF

