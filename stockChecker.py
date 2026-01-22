import urllib.request
import json

part = "MTXJ3LL/A"   # test part
zip_code = "24060"

url = f"https://www.apple.com/shop/fulfillment-messages?pl=true&parts.0={part}&location={zip_code}"

print("Checking URL:", url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        data = resp.read().decode('utf-8')
        parsed = json.loads(data)
        print("Status:", resp.status)
        print("\nPretty JSON:")
        print(json.dumps(parsed, indent=2))
except Exception as e:
    print("Error:", e)