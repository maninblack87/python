import urllib.request as request
import json

json_str = request.urlopen("http://api.github.com/repositories").read()
output = json.loads(json_str)

for item in output:
    print(item["name"])
    print(item["full_name"])
    print(item["owner"]["login"])
    print()
