passwords = {
    'email': 'Phoenix@246',
    'vtu': 'Phoenix2',
    'github': 'Phoenixshri@246',
    'microsoft': 'Sharky@246',
    'ssp': 'Phoenix246'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pswdlck.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('there is no password for ' + account)