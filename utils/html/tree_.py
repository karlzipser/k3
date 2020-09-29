from k3 import *

style = """
<style>
/* Remove default bullets */
ul, #myUL {
  list-style-type: none;
}

/* Remove margins and padding from the parent ul */
#myUL {
  margin: 0;
  padding: 0;
}

/* Style the caret/arrow */
.caret {
  cursor: pointer; 
  user-select: none; /* Prevent text selection */
}

/* Create the caret/arrow with a unicode, and style it */
.caret::before {
  content: "\\25B6";
  color: black;
  display: inline-block;
  margin-right: 6px;
  -ms-transform: rotate(90deg); 
  -webkit-transform: rotate(90deg); 
  transform: rotate(90deg);
}

.caret-down::before {
  -ms-transform: rotate(0deg); 
  -webkit-transform: rotate(0deg); 
  transform: rotate(0deg);  
  ;
}

/* Hide the tree_nested list */
.tree_nested {
  display: block;
}

/* Show the tree_nested list when the user clicks on the caret/arrow (with JavaScript) */
.tree_active {
  display: none;
}
</style>
"""

script = """
<script>
var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".tree_nested").classList.toggle("tree_active");
    this.classList.toggle("caret-down");
  });
}
</script>
"""

button = """
<form action="" >
  <label for="files_dir">Top Path</label>
  <input style="font-size:14px;" type="text" id="files_dir" name="files_dir" value="FILES_DIR">
  <input hidden readonly type="text" id="city_tab" name="city_tab" value=\"Files\">
  <input  type="submit" value="Submit">
</form>
"""



def get_tree(p):

  p = p.replace(opjh(),'')
  if p[-1] == '/' and len(p) > 1:
    p = p[1:]

  s = [style,button.replace('FILES_DIR',p),"<ul id='myUL'>"]


  D = {}
  #p = pname(p)
  #cy(p,files_to_dict2(opjh(p)),r=1)
  D = {p:files_to_dict(opjh(p))}

  #kprint(D)

  def a(D):
    if type(D) is dict:
        for k in kys(D):
            if '__pycache__' in k:
                continue
            if k != '__init__.py' and k[0] == '_':
                continue
            if k != '.':
                s.append(d2s("<li><span class='caret'>"+fname(k)+"</span>"))
                s.append(d2s("<ul class='tree_nested'>"))
                
            a(D[k])
            if k != '.':
                s.append(d2s('</ul></li>'))
    elif type(D) is list:
        for e in D:
            if exname(e) not in ['js','py','html','txt','c','cpp']:
                continue
            s.append(d2s("<li><a href='"+e.replace(opjh(),'/')+"?city_tab=Files'>",fname(e),"</a></li>"))

  #d2n('\n<a '+u+' href=',qtd(dst),'>',s,'</a>\n')

  a(D)

  #zprint(D)
  s.append(script)
 
  #text_to_file(opjD('temp.html'),'\n'.join(s))

  return '\n'.join(s)#,D


#EOF
