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
def parse_instructions():
    #  URL PARSING
    # LINK: https://stackoverflow.com/questions/6594620/python-3-2-unable-to-import-urllib2-importerror-no-module-named-urllib2
    server_address = url_prefix + "192.168.1.112:3000" + "/" + file_name

    wp = urllib.request.urlopen(server_address)
    pw = wp.read()
    data = json.loads(pw)

    print(data["client_instructions"]["date"])
    # print(pw)


parse_instructions()
