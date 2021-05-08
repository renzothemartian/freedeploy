import sys
import subprocess
import uuid
import platform


#  Execute bash command
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def shell_task(_task):
    process = subprocess.Popen(_task, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(f'task return code: {process.returncode}')
    return process


def get_python_version():
    # Python Version Check
    p_version = sys.version_info[0]
    # if pythonVersion >= 3:
    #     print(f"Running Py3: {pythonVersion}")
    return p_version

def get_mac_addy():
    a = platform.system()
    if a != ("Darwin"):
        print("its not mac")
    # CHECK SYSTEM PLATFOMR
    # IF LINUX PRINT ME SOME STUFF




get_mac_addy()
