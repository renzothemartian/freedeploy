import sys
import urllib
import urllib.request
import json

url_prefix = "http://"
file_name = "client_instructions.json"
# Python Version Check
pythonVersion = sys.version_info[0]
if pythonVersion >= 3:
    print(f"Running Py3: {pythonVersion}")

data = ""
# this hits a URL and Saves the response


def parse_instructions():
    #  URL PARSING
    # LINK: https://stackoverflow.com/questions/6594620/python-3-2-unable-to-import-urllib2-importerror-no-module-named-urllib2
    server_address = url_prefix + "192.168.1.112:3000" + "/" + file_name

    wp = urllib.request.urlopen(server_address)
    pw = wp.read()
    data = json.loads(pw)

    print(data["client_instructions"]["date"])
    do_datas(data)
    # print(pw)

# doing things
def do_datas(_data):
    print(f"data: {_data}")


# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()



parse_instructions()
# do_datas()