x = input()
import urllib2
response = urllib2.urlopen(server)
data = response.read()
print(data)
# with open('data.txt', 'r') as inps:
#     print(inps.read())