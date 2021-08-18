import requests
from pprint import pprint
import json
from postcode_task import PostCode
postcode_url = "https://api.postcodes.io/postcodes/"
#postcode_request = requests.get(postcode_url + "B7 4BB")

#print(postcode_request)
#print(postcode_request.headers, type(postcode_request.headers))
#print(postcode_request.content, type(postcode_request.content))

#print(postcode_request.json())
#pprint(postcode_request.json())

postcodes = {'postcodes' : ["PR3 0SG", "M45 6GN", "EX16 5BL"]}
body = json.dumps(postcodes)
headers = {'Content-Type': 'application/json'}

multi_pc = requests.post(postcode_url, headers=headers, data=body)
#print(multi_pc)
multi_pc_result = multi_pc.json()['result']
#pprint(multi_pc_result, sort_dicts=False)

for postcode in multi_pc_result:
    pc = PostCode(postcode['result'])
    print(pc)
    print(pc.lat, pc.long)
    print(pc.get_location())