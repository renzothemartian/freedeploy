import subprocess
import sys
import urllib
import urllib.request as req
import json

url_prefix = "https://"
file_name = "client_instructions.json"
test_url = f"{url_prefix}raw.githubusercontent.com/renzothemartian/freedeploy/main/serber/{file_name}"

data = ""

# Python Version Check
pythonVersion = sys.version_info[0]
# if pythonVersion >= 3:
#     print(f"Running Py3: {pythonVersion}")

#  Execute bash command


def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


# this hits a URL and Saves the response
def parse_instructions(_url=None):
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
    # print(_inst['upgrade'])
    # b_cmd = 'sudo apt update'

    # # wait for it to finish
    # for _val in _inst['install']:
    #     print(f'value:{_val}')

    # for key, value in _inst['install'].items():
    #         print(f"key: {key} val: {value}")

    bashCommand = "echo hello there friendo"
    bash_command(bashCommand)
    # process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()


















# parse_instructions(<YOUR URL HERE>)
parse_instructions()
# do_datas()
