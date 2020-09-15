from k3 import *
from urllib.parse import unquote
from k3.drafts.htmltemp import *

select = """

<form>
<select name='get_page' onchange='this.form.submit()'>
  <option>get_page</option>
  <option>get_page0</option>
  <option>get_page1</option>
  <option>get_page2</option>
</select>
<noscript><input type="submit" value="Submit"></noscript>
</form>
"""


# python k3/utils/core/paths.py | tee Desktop/out.txt

def get_page1(path,URL_args):
    
    s = head_('this is the title')

    s += select

    s += br*2

    s += l2h(d2n("You accessed path: ",path,''))

    s += br*2

    s += l2h(d2n("You accessed path: ",unquote(path)))
        
    s += br*2
    
    s += l2h('   some text! •¶§∞¢')

    s += br

    s += href_(
        '/',
        img_('/Pictures/IMG_5362.jpeg',"width:200px;"), 
    )

    s += br

    s += href_('/page1/?path=ads/bfe/ca/&get_page=get_page1','suck it up')

    s += br

    s += href_(
        '?this_images_points_to=this_text&q=w&n=1&get_page=get_page2&code=k3/scripts/gen/temperature.py',
        img_('/Pictures/me.png',"width:100px;"), 
    )

    s += br

    s += href_("?a=a/b/c/&get_page=get_page1",'suck it up 2')

    s += br

    s += form_('get_page')

    s += br

    s += br

    

    #s += end_()

    return s


def get_page0(path,URL_args):
    s = head_('this is the title')
    s += select

    s += br*2
    s += l2h(d2n("You accessed path: ",path,''))
    s += br*2
    s += 'begin'
    s += br*2
    s += form_('get_page')
    #s += select
    #s += end_()


    return s

# importlib.reload(module)
kin = k_in_D
def get_page2(path,URL_args):

    if kin('code',URL_args):
        code = highlight(file_to_text(URL_args['code']), PythonLexer(), HtmlFormatter())
    s = head_('this is the title')
    s += style
    s += select
    s += br*2
    s += l2h(d2n("You accessed path: ",path,''))
    s += br*2
    s += 'end'
    #s += select
    #s += end_()
    if kin('code',URL_args):
        s += '<h1>'+URL_args['code']+'</h1>'
        s += code
    return s

G = {
    'get_page0':get_page0,
    'get_page1':get_page1,
    'get_page2':get_page2,
}



#EOF
