import subprocess
import uuid

#  Execute bash command
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

# after each 2 digits, join elements of getnode().
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))
