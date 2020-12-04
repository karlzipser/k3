#,a

F = find_files_recursively(opjh('Movies'),'*.mp4',FILES_ONLY=True)
l = []
m = []
if 'o' not in locals():
    o = []
for p in F['paths']:
    for f in F['paths'][p]:
        #clp(p,'`r--',f,'`g--')
        
        assert (p,f) not in l
        g = opj(F['src'],p,f)
        l.append((p,f))
        if f in m or g in o:
            continue
        else:
            m.append(f)
        
        n = len(sggo(g))
        assert n == 1
        os_system('open',qtd(g))
        os_system(""" osascript -e 'tell application "Terminal" to activate' """,e=0)
        y = raw_enter('1 or 0')
        if y == '1':
            o.append(g)
            cg(o)


#,b
