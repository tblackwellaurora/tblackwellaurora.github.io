import requests
import json

from flask import Flask, request, abort
app = Flask(__name__)
@app.route('')

url = "https://api-sandbox.aurorasolar.com/tenants/16d565a6-1bce-4ccb-b322-a5b89c3527c2/webhooks"

payload = json.dumps({
  "webhook": {
    "event": "project_created",
    "url_template": "https://webhook.site/247dbae2-d3a1-4fb1-9e04-183f8a5b6423/project_created",
    "description": "Aurora Reverse Geocode",
    "enabled": True
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer sk_sand_e3cccb9b7236924b258488bc',
  'Cookie': '_aurorasolar_session=ZDdqQ3BXU1d2NnBWZVRMQjVZQmZkaUZsQ2EvbFIvUFJXanRDajY5NHVFblQ2RnBOcFIwTVVsSWtMMUxGUm5HNnZDWDl2Z0ZLMFA0b1BIdTc1cUExTzNyaVVwWnpmMW9nV0FiRDE1K2FjazU2bU9yOVBja2VOMHhIaTkzQ2JvZystLWdhZUJCS2IwajRuQmJUaHQrdUpoWGc9PQ%3D%3D--3a54e298ad7f787ac47c632c9c54c48d458d530a'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



# webhook_url = 'https://webhook.site/247dbae2-d3a1-4fb1-9e04-183f8a5b6423'

# data = { 'name': }