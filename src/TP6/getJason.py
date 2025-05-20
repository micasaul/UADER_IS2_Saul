import json
import sys

jsonfile = 'sitedata.json'
jsonkey = sys.argv[1] if len(sys.argv) > 1 else 'token1'

with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

print(str(obj[jsonkey]))