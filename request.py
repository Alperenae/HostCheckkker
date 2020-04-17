import requests
# This Is a Basic http/https request Script. :)
url = input("Enter The Url: ")
if url == "" :
    print("-----------------")
    print ("ERROR!")
    print("-----------------")
#---------------------------
r = requests.get(url)
print ("------------------------------------------------------")
print ("| Response:",r.status_code)
print ("------------------------------------------------------")
print ("| Header:",r.headers)
print ("------------------------------------------------------")
