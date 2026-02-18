
import requests
import time

part_number = "MFXH4LL" #hard coded for now 
zip_code = "20171"
# Use either endpoint variant
url = "https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0=MFXH4LL%2FA&location=20171"

response = requests.get(url)
for i in range(1):
    response = requests.get(url)

    print(response.status_code)
    print(response.json())
# webhook_url = "https://discord.com/api/webhooks/1472440491567087789/_kHlDe4i0a1Xwro5FPqGBVeIpyvpXYWXzJkFUWZ3lOIqMgEm0ef69qcFFWpu54faQMLr"
# requests.post(webhook_url, json={"content": "iPhone available!"})