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

#,a
txt = "<cello abc def><quartet>"
open_tag = "<([a-z|A-Z]+)(.*?)>"
x = re.findall(open_tag,txt)


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

#EOF

