import sys
import os
import site

if sys.prefix != sys.base_prefix:
    print(f"""\nMATRIX STATUS: Welcome to the construct

Current Python: {os.getcwd()}
Virtual Environment: matrix_env
Environment Path: {sys.executable}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
{site.getusersitepackages()}
""")
else:
    print(f"""\nMATRIX STATUS: You're still plugged in

Current Python: {sys.executable}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.
""")