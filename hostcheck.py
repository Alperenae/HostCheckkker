import argparse
import requests
import time

# Colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


parser = argparse.ArgumentParser('', 'python3 test.py -u --url')    
parser.add_argument('-u', '--url', type=str, required=True, help='Target')
args = parser.parse_args()

print(WARNING + "\n [*] Respons is Waiting" + ENDC)
r = requests.get(args.url)

if r.status_code == 200:
    time.sleep(3)
    print ("\n --------------")
    print (OKGREEN + "\n Host Up Yey!" + ENDC)
    print ("")
    print ("--------------")

else:
    print( FAIL + "\n Host Down Shitt !" + ENDC)
