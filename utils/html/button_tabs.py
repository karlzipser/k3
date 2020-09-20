from k3 import *
from k3.utils.html.tags import *


button_script = """

	<script>
	function openCity(evt, cityName) {
	  var i, tabcontent, tablinks;
	  tabcontent = document.getElementsByClassName("tabcontent");
	  for (i = 0; i < tabcontent.length; i++) {
	    tabcontent[i].style.display = "none";
	  }
	  tablinks = document.getElementsByClassName("tablinks");
	  for (i = 0; i < tablinks.length; i++) {
	    tablinks[i].className = tablinks[i].className.replace(" active", "");
	  }
	  document.getElementById(cityName).style.display = "block";
	  evt.currentTarget.className += " active";
	}
	</script>
	"""

button_style = """
	<style>
	body {font-family: Arial;}

	/* Style the tab */
	.tab {
	  overflow: hidden;
	  border: 1px solid #ccc;
	  background-color: #f1f1f1;
	}

	/* Style the buttons inside the tab */
	.tab button {
	  background-color: inherit;
	  float: left;
	  border: none;
	  outline: none;
	  cursor: pointer;
	  padding: 14px 16px;
	  transition: 0.3s;
	  font-size: 17px;
	}

	/* Change background color of buttons on hover */
	.tab button:hover {
	  background-color: #ddd;
	}

	/* Create an active/current tablink class */
	.tab button.active {
	  background-color: #ccc;
	}

	/* Style the tab content */
	.tabcontent {
	  display: none;
	  padding: 6px 12px;
	  border: 1px solid #ccc;
	  border-top: none;
	}
	</style>
	"""


def button_tabs(
	Buttons,
	button_script=button_script,
	button_style=button_style,
):
	tab_ = 'tab'
	tablinks = 'tablinks'
	tabcontent = 'tabcontent'
	html = button_style
	buttons,div_content = '',''

	for b in sorted(Buttons):
		if Buttons[b][:2] == '#!':
			onclick = Buttons[b][2:]
		else:
			onclick = "openCity(event, '"+b+"')"
		buttons += button(class_=tablinks,
					onclick=onclick,
					content=b)
		div_content += div(id=b,class_=tabcontent,content=Buttons[b])+'\n'

	html += div(class_=tab_,
		content=buttons)

	html += div_content

	html += button_script

	return html

Arguments = get_Arguments({})

def main(**A):

	html = editor_head

	html += editor


	html += """

<div class="sidebar" style="
    margin:0;
    width:500px;
    height:790;
    float: right !important;
    margin-right:20px;
    margin-left:20px;
    position:relative;
    padding: 0;
    text-align: left;
    font-family:'Courier New';
    font-size:14px
    overflow-y: scroll;"
>


	"""

	html += button_tabs(
		{
			'London':'London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.',
			'New York':'New York pital city of England.',
			'Berlin':'Berlin adsfasdfdsfd city of England.',
			'Save':"#!alert('This could save data');",
		},
	)

	html += save_button

	html += '</div>'

	text_to_file(opjD('temp3.html'),html)


if __name__ == '__main__':
	main(**Arguments)


#,b

#EOF

