import requests
import json

new_file = 'cso.json'

jsonrpc_request = {
    "jsonrpc": "2.0",
    "method": "PxStat.Data.Cube_API.ReadDataset",
    "params": {
        "class": "query",
        "id": [],
        "dimension": {},
        "extension": {
            "pivot": None,
            "codes": False,
            "language": {"code": "en"},
            "format": {"type": "JSON-stat", "version": "2.0"},
            "matrix": "FIQ02",
        },
        "version": "2.0",
    },
}

response = requests.post('https://ws.cso.ie/public/api.jsonrpc', json=jsonrpc_request)

if response.status_code == 200:
    with open(new_file, 'w') as file:
        file.write(response.text)
    print(f"Data successfully saved to '{new_file}'")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
