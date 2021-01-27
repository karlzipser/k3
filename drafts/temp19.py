
#,a
import nltk
from striprtf.striprtf import rtf_to_text 

p = '/Users/karlzipser/Desktop/_2008 one -- Editing version 12-27-2020'  
rs = sggo(p,'*.rtf')

def get_text(rs):
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
    return b


def get_Count(text):
    c = []
    for d in text: 
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
    print(type(g),len(g))
    return len(g),C



Texts = {
    'full_text':get_text(rs)
}
for r in rs:
    if fname(r)[0] == '_':
        continue
    Texts[fname(r)] = get_text([r])    

Counts = {}
Word_counts = {}
Freqs = {}

for t in Texts:
    Word_counts[t],Counts[t] = get_Count(Texts[t])

for t in Texts:
    Freqs[t] = {}
    for w in Counts[t]:
        Freqs[t][w] = Counts[t][w]/Counts['full_text'][w]
#,b

gg = nltk.word_tokenize(e)
ggg = nltk.pos_tag(gg)


