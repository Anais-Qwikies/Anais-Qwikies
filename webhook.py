import requests
import json

webhook_url = 'https://webhook.site/5364a595-6b43-4b6e-9ba1-b11e272a140f'
data = { 'name' : 'nighthack' ,
         'message' : 'Hello World' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



