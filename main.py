import platform
import os
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sys_info():
    uname = platform.uname()
    print("===== System info =====")
    print(f"System: {uname.system} \tMachine name: {uname.node}")
    print(f"Wydanie: {uname.release} \tVersion: {uname.version}")
    print(f"Machine: {uname.machine} \tProcessor: {uname.processor}")


def check():
    os.system('cls')
    print("="*10)
    ip_to_check = input("Insert IP address:")
    print()
    os.system("ping {}".format(ip_to_check))
    input("D")

def ping_ip(ip):
    (output, error) = subprocess.Popen((['ping', ip, '-n', '1']), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,).communicate()
    if b'bytes=32'in output:
        return bcolors.OKGREEN + bcolors.BOLD + "In work" + bcolors.ENDC
    elif b'Destination host unreachable.' in output:
        return bcolors.FAIL + ".. No response" + bcolors.ENDC
    elif error:
        return bcolors.WARNING + " - Error DNS -" + bcolors.ENDC
    else:
        return bcolors.OKBLUE + "Unknown" + bcolors.ENDC


addr = input("Inpus IP address (e.g. 000.000.000.): ")
a = int(input("Start address scan from 1 to 255:"))
b = int(input("Stop address scan from 1 to 255:"))

for ip in range(a, b+1):
    ip = str(addr) + "." + str(ip)
    ip = ip.strip('\n')
    response = ping_ip(ip)
    result = ('> %s %s' % (ip, response))
    print(result)
