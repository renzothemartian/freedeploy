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
    system_utils.get_mac_addy()
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
    # Write data to console
    # print(data["client_instructions"]["server_ip"])
    # this is going to do things
    do_datas(data)
    # print(response)


# doing things
def do_datas(_data):
    for key, value in _data['client_instructions'].items():
        if key == 'instructions':
            # print(f"key: {key} val: {value}")
            do_instructions(value)


def do_instructions(_inst):
    print(f'instructions: {_inst}')
    # print(_inst['upgrade'])
    # b_cmd = 'sudo apt update'

    # # wait for it to finish
    for _val in _inst['install']:
        # print(f'value:{_val}')
        install_programs(_val)
    # for key, value in _inst['install'].items():
    #         print(f"key: {key} val: {value}")

    my_cmd = "echo hello there friendo"
    system_utils.bash_command(my_cmd)





install_cmd_prefix = 'sudo apt install '
def install_programs(_program):
    _cmd = install_cmd_prefix + _program
    print(f'i: {_cmd}')
    # system_utils.bash_command(my_cmd)






# get_instructions(<YOUR URL HERE>)
get_instructions()
# do_datas()
