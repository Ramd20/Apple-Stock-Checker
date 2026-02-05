
import requests
import time

part_number = "MFXH4LL" #hard coded for now 
zip_code = "20171"
# Use either endpoint variant
url = "https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0=MFXH4LL%2FA&location=20171"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.apple.com/shop/buy-iphone/iphone-17-pro",  # Important: match product page
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
}

for i in range(1):
    response = requests.get(url)
    print(str(i) + ":" + str(response.status_code)) #7 min unban
    time.sleep(5)
