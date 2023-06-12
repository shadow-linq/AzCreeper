import requests
import json
import sys

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("azcreeper.py <DOMAIN> <USERLIST>")
  domain = sys.argv[1]
  f = open(sys.argv[2], "r")
  users = f.read().split('\n')
  for user in users:
    email = user
    if "@" not in email:
      email += "@" + domain
    r = requests.post("https://login.microsoftonline.com/common/GetCredentialType", json={"Username":email})
    r = json.loads(r.text)
    if r["IfExistsResult"] == True or r["Credentials"]["CertAuthParams"] != None:
      print(f"{email} exists")
