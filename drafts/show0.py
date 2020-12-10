#!/usr/bin/env python3

"""#,s1a

python3 k3/drafts/archive0.py

#,s1b"""

Arguments = get_Arguments(
    Defaults={
        'src':opjD(),
        'dst':opjh('Archived'),
        'window_width' : 500,
        'window_height' : 500,
        'ignore_underscore':True,
    }
)


def find(src,pattern,e=0,r=0,a=1):
    tempfile = opjD(d2p('find','temp',random_with_N_digits(9),'txt'))
    os_system('find',src,'-name',qtd(pattern),">",tempfile,e=e,r=r,a=a)
    find_list = txt_file_to_list_of_strings(tempfile)
    os_system("rm",tempfile)
    return find_list


fs = find(opjh('Archived'),'_preview.jpg',e=1) 
imgs = []
padval = 127
blank = zeros((400,400,3),np.uint8)
for f in fs:
    img = zimread(f)
    h,w,d = shape(img) 
    blank = 0 * blank + padval
    blank[:h,:w,:d] = img
    imgs.append(blank)

mi(vis_square2(imgs,padsize=8,padval=padval),3)
spause()




def file_type(f):
    e = exname(f)
    e = e.lower()
    Q = {
        'jpg':'jpg',
        'jpeg':'jpg',
        'png':'png',
        'tiff':'tiff',
        'gif':'gif',
        'pdf':'pdf',
        'rtf':'rtf',
        'txt':'txt',
    }
    if e in Q:
        return Q[e]
    else:
        return 'unknown'





def assert_link_is_valid(f):
    if len(sggo(f)) == 1:
        return True
    else:
        return False

#def assert_archive_link_is_valid(f):

if __name__ == '__main__':

    archive(Arguments)

#EOF
