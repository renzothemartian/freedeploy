import subprocess
import sys
import urllib
import urllib.request as req
import json

import system_utils

url_prefix = "https://"
file_name = "client_instructions.json"
test_url = f"{url_prefix}raw.githubusercontent.com/renzothemartian/freedeploy/main/serber/{file_name}"


# this hits a URL and Saves the response
def get_instructions(_url=None):
    # print(f"PYTHON: {system_utils.get_python_version()}")
    #  URL PARSING
    
    # Null check on _url param
    if _url == "" or _url == None:
        # print(f"if: {server_address}")
        server_address = test_url
    else:
        # print(f"else: {server_address}")
        server_address = _url

    # send web request
    request = req.urlopen(server_address)

    # read data (Response)
    response = request.read()

    # save data as JSON variable
    data = json.loads(response)

    # this is going to do things
    do_datas(data)

    # print(response)
    with open('instructions.json', 'w') as outfile:
        json.dump(data, outfile)



# doing things
def do_datas(_data):
    for key, value in _data['client_instructions'].items():
        if key == 'instructions':
            # print(f"key: {key} val: {value}")
            do_instructions(value)


def do_instructions(_inst):

    # print(f'instructions: {_inst}')
    if system_utils.get_system_type() == ("Linux"):
        a = system_utils.shell_task('sudo apt update')
        if a.returncode == (0):
            print ("update/upgrade succesful using apt")
        else:
            print ("process failed")
        print("it is linux")

    else:
        print("not linux")

    #  wait for it to finish
    for _val in _inst['install']:
        # print(f'value:{_val}')
        install_programs(_val)


install_cmd_prefix = 'sudo apt install '
def install_programs(_program):
    _cmd = install_cmd_prefix + _program
    # print(f'i: {_cmd}')
    # system_utils.bash_command(my_cmd)
 


# get_instructions(<YOUR URL HERE>)
get_instructions()