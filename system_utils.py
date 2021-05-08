import sys
import subprocess
import uuid

#  Execute bash command
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def shell_task(_task):
    process = subprocess.Popen(_task, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)
    return process


def get_python_version():
    # Python Version Check
    p_version = sys.version_info[0]
    # if pythonVersion >= 3:
    #     print(f"Running Py3: {pythonVersion}")
    return p_version

def get_mac_addy():
    print('oo')


get_mac_addy()
