import sys
import subprocess
import uuid

#  Execute bash command
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def get_python_version():
    # Python Version Check
    p_version = sys.version_info[0]
    # if pythonVersion >= 3:
    #     print(f"Running Py3: {pythonVersion}")
    return p_version

def get_mac_addy():
    


get_mac_addy()
