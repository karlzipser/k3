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
		buttons += button(class_=tablinks,
					onclick="openCity(event, '"+b+"')",
					content=b)
		div_content += div(id=b,class_=tabcontent,content=Buttons[b])+'\n'

	html += div(class_=tab_,
		content=buttons)

	html += div_content

	html += button_script

	return html


def main(**A):
	html = button_tabs(
		{
			'London':'London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.London is the capital city of England.',
			'New York':'New York pital city of England.',
			'Berlin':'Berlin adsfasdfdsfd city of England.',
			'Berlin2':'Berlin2 adsfasdfdsfd city of England.',
		},
	)
	text_to_file(opjD('temp3.html'),html)


if __name__ == '__main__':
	main()


#,b

#EOF

