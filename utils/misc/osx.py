from k3.utils.misc.sys import *


def quit_Preview():
    os_system(""" osascript -e 'quit app "Preview"' """)
    return

def close_Finder_windows():
    os_system(""" osascript -e 'tell application "Finder" to close every window' """)
    return

    
#EOF
