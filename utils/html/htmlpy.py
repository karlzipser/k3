from k3 import *
from urllib.parse import unquote

def urlparse(url):
    URL_args = {}
    a = url
    b = a.split('?')
    path = b[0]
    if len(b) > 1:
        c = b[-1]
        #cg(c)
        d = c.split('&')
        for e in d:
            if e is not None:
                f = e.split('=')
                #print(f)
                f[1] = f[1].replace('+',' ')
                f[1] = unquote(f[1])
                #print(f[1])
                URL_args[f[0]] = f[1]
    #if path[0] == '/':
    #    path = path[1:]
    return path,URL_args

sp = '&nbsp'

br = '<br>\n'
def lines_to_html_str(print_lines):
    if type(print_lines) == str:
        print_lines = print_lines.split('\n')
    assert type(print_lines) == list
    h = '\n<br>'.join(print_lines).replace(' ','&nbsp').encode('ascii', 'xmlcharrefreplace').decode('utf8')
    replace_list = list(range(100))
    for i in rlen(replace_list):
        replace_list[i] = d2n('[',replace_list[i],'m')
    for s in replace_list:
        h = h.replace(s,'')
    return h
l2h = lines_to_html_str

def head_(s):
    a = """
<html>
<head>
<title>
        """
    b = """
</title>
</head>
<body>
        """
    return a + s + b


def img_(src,style):
    return d2n('\n<img src=',qtd(src),' style=',qtd(style),'>\n')


def href_(dst,s,underline=False):
    if not underline:
        u = "style='text-decoration:none'"
    else:
        u = ''
    return d2n('\n<a '+u+' href=',qtd(dst),'>',s,'</a>\n')


def form_(s,v=''):
    return """\n<form action="" method="GET">\n""" + \
        s + " <input size='50' type='text' name='"+get_safe_name(s)+"' value='"+v+"''>\n" +\
        "</form>\n"


def end_():
    return "\n</body></html>\n\n"

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

style = """
<style>
.highlight .hll { background-color: #ffffcc }
.highlight  { background: #ffebcd; } /*#f8f8f8; }*/
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
</style>
"""
#border-color: coral;
def div(px):
    return """
<div
    style="
        overflow-y: scroll;
        height:"""+str(px)+"""px;
        font-family:'Courier New';
        font-size:12px"
border-right: 1px solid #000;
border-left: 1px solid #000;
>
    """
#EOF

