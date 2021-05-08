import sys
import subprocess
import uuid
import platform

# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/





#  Execute bash command
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def shell_task(_task):
    process = subprocess.Popen(_task, shell=True, text=True,stdout=subprocess.PIPE)
    process.wait()
    # print(f'task return code: {proc.ess.returncode}')
    return process




def get_python_version():
    # Python Version Check
    p_version = sys.version_info[0]
    # if pythonVersion >= 3:
    #     print(f"Running Py3: {pythonVersion}")
    return p_version


# CHECK SYSTEM PLATFOMR
def get_system_type():
    a = platform.system()
    # if a == ("Darwin"):
    #     print(f"its a mac: {a}")
    # if a == ("Linux"):
    #     print(f"its linux: {a}")
    # if a == ("Windows"):
    #     print(f"its linux: {a}")
    return a


def get_mac_address():
    a = get_system_type()
    _cmd = ''
    if a == ("Linux"):
        _active_network_type = "ip addr show | awk '/inet.*brd/{print $NF}'"
        cc = shell_task(_active_network_type).stdout.read()
        _cmd = f'ip addr show {cc}'
    if a == ("Darwin"):
        _cmd = "ifconfig en1 | awk '/ether/{print $2}'"

    # bash_command(_cmd)
    bb = shell_task(_cmd).stdout.read()
    print(f"MAC Address: {bb}")


get_mac_address()
