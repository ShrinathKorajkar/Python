# usage: py multicp.py save <keyword> - saves clipboard to keyword
#       py multicp.py <keyword> - loads keyword to clipboard
#       py multicp.py list - loads all keywords to clipboard

import shelve, pyperclip, sys, os

os.chdir(os.path.dirname(__file__))
mcb = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb.keys())))
    elif sys.argv[1] in mcb:
        pyperclip.copy(mcb[sys.argv[1]])
mcb.close()
