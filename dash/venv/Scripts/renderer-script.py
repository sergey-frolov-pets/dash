#!c:\flask\dash\dash\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'dash==1.13.4','console_scripts','renderer'
__requires__ = 'dash==1.13.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dash==1.13.4', 'console_scripts', 'renderer')()
    )
