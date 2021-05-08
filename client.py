import sys
import urllib
import urllib.request
import json

url_prefix = "https://"
file_name = "client_instructions.json"
test_url = f"{url_prefix}raw.githubusercontent.com/renzothemartian/freedeploy/main/serber/{file_name}"

data = ""
# Python Version Check
pythonVersion = sys.version_info[0]
# if pythonVersion >= 3:
#     print(f"Running Py3: {pythonVersion}")

# this hits a URL and Saves the response


def parse_instructions(_url=None):
    #  URL PARSING
    # Null check on _url param
    if _url == "" or _url == None:
        # server_address = url_prefix + "192.168.1.112:3000" + "/" + file_name
        server_address = test_url
        print(f"if: {server_address}")
    else:
        server_address = _url
        print(f"else: {server_address}")

    # do the req
    wp = urllib.request.urlopen(server_address)
    # read the data
    pw = wp.read()
    # save data as JSON variable
    data = json.loads(pw)
    # Write data to console
    print(data["client_instructions"]["server_ip"])
    # this is going to do things
    do_datas(data)
    # print(pw)

# doing things


def do_datas(_data):
    # print(f"data: {_data}")
    print()


# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()


# parse_instructions("https://raw.githubusercontent.com/renzothemartian/freedeploy/main/serber/client_instructions.json")
parse_instructions()
# do_datas()
