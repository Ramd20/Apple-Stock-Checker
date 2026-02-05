
import requests
import json

part_number = "MFXP4LL"
zip_code = "19720"
# Use either endpoint variant
#MFXP4LL/A -> 1tb Orange
url = f"https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0={part_number}%2FA&location={zip_code}"

print(url)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Referer": "https://www.apple.com/shop/buy-iphone/iphone-17-pro",  # Important: match product page
#     "Accept-Language": "en-US,en;q=0.9",
#     "Connection": "keep-alive"
# }

try:
    response = requests.get(url, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2)) #this makes it look nicer
    elif response.status_code == 541:
        print("541 error - likely rate limit or blocked. Wait 5-10 min, try VPN, or add more delays.")
    else:
        print(f"Error: {response.status_code} - {response.text[:300]}")
except Exception as e:
    print(f"Request failed: {e}")


