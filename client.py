import sys
import urllib
import urllib.request

# Python Version Check
pythonVersion = sys.version_info[0]
if pythonVersion >= 3:
    print(f"Running Py3: {pythonVersion}")
    #  URL PARSING
    # LINK: https://stackoverflow.com/questions/6594620/python-3-2-unable-to-import-urllib2-importerror-no-module-named-urllib2
    server = "https://robotrenzo.com"
    wp = urllib.request.urlopen(server)
    pw = wp.read()
    print(pw)
