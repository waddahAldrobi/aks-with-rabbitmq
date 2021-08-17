import requests
import json

# external_ip = # EXTERNAL_IP
external_ip = '52.191.19.255'
endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/syncAnalyze?language=en&readingOrder=natural'

file = 'https://raw.githubusercontent.com/mdrakiburrahman/form-recognizer/main/artifacts/mortgage.pdf'
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         })

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))