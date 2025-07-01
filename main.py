import requests
import json
from pprint import pprint
from config_payload import switch_config
from config_payload import headers

url = f"https://{switch_config['host']}:{switch_config['port']}/restconf/data/ietf-interfaces:interfaces"

body = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback77",
    "type" : "iana-if-type:softwareLoopback",
    "enabled" : "true",
    "ietf-ip:ipv4" : {
        "address" : [
            {
            'ip' : '198.51.100.77',
            'netmask' : '255.255.255.0'
            }
        ]
    }
}
})

response = requests.request('POST', url, headers=headers, auth=(switch_config['user'], switch_config['password']), data=body, verify=False)

status_code = str(response.status_code)
print(status_code)

if status_code.startswith('2'):
    url = f"https://{switch_config['host']}:{switch_config['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"
    body = json.dumps({})
    response = requests.request('GET', url, headers=headers, auth=(switch_config['user'], switch_config['password']), data=body, verify=False)
    print("""
*******************************
Interface Addition has been
        successful
*******************************         
""")
    api_data = response.json()
    print(f"""
RAW RESPONSE-------
{pprint(api_data, indent=2)}
          """)
else:
    print("****Interface has not been addedd****")

if status_code.startswith('2'):
    url = f"https://{switch_config['host']}:{switch_config['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"
