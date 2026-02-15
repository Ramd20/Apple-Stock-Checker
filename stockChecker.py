
import requests
import json
import time

part_number = "MFXG4LL"
zip_code = "97002"
# Use either endpoint variant
#MFXP4LL/A -> 1tb Orange
#MFXN4LL -> 1tb Silver
#MFXG4LL -> 256GB Silver
url = f"https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0={part_number}%2FA&location={zip_code}"

print(url)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Referer": "https://www.apple.com/shop/buy-iphone/iphone-17-pro",  # Important: match product page
#     "Accept-Language": "en-US,en;q=0.9",
#     "Connection": "keep-alive"
# }

while True:
    response = requests.get(url, timeout=10)
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        body = data["body"]
    

        if "stores" in body: #making sure zip code is valid    
        
        

            # for store in body["stores"]:
            #     print(store["storeName"], store["state"])

            #     partsAvailability = store["partsAvailability"] #digs through json to get availability
            #     modelInfo = partsAvailability[part_number + "/A"]
                
            #     print(modelInfo["pickupDisplay"]) #shows available or unavailable
            #     print(" ")        

            firstStore = body["stores"][0]

            if firstStore["state"] == "OR": #remove the hardcoding and change to softcoding later
                print(firstStore["storeName"])
                print("available")                #first store is 99 percent of the time an available store
                
            else:
                print("unavailable")
    
        
        else:
            print("invalid zip code")


    elif response.status_code == 541:
        print("541 error - likely rate limit or blocked. Wait 5-10 min, try VPN, or add more delays.")
    else:
        print(f"Error: {response.status_code} - {response.text[:300]}")


    time.sleep(600)