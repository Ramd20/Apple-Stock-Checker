
import requests
import json
import time
import os
from dotenv import load_dotenv


load_dotenv()
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
part_number = "MFXN4LL"
zip_code = "19720"
# Use either endpoint variant
#MFXP4LL/A -> 1tb Orange
#MFXN4LL -> 1tb Silver
#MFXG4LL -> 256GB Silver

#christiana store -> R102
storeNumber = "R102"
url = f"https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0={part_number}%2FA&location={zip_code}"
storyeUrl = f"https://www.apple.com/shop/retail/pickup-message?pl=true&parts.0={part_number}%2FA&store={storeNumber}"


print(url)

def checkSingleStore(partNumber, storeNumber):
    storeUrl = f"https://www.apple.com/shop/retail/pickup-message?pl=true7&parts.0={partNumber}%2FA&store={storeNumber}"
    try:
        response = requests.get(storeUrl, timeout=10)
        print(response.status_code)#DEBUG STATEMENT
        if response.status_code == 200:
            data = response.json()
            body = data["body"]

            if "stores" in body: #making sure zip code is valid    
            
        
                specificStore = body["stores"][0]

                availability = specificStore["partsAvailability"][f"{part_number}/A"]["pickupDisplay"]

                return {
                    "status": availability,
                    "name": specificStore["storeName"],
                    "error": None
                }
            else:
                return {
                        "status": "error",
                        "name": None,
                        "error": "No stores in response"
                    }
        
        elif response.status_code == 541:
            return {
                    "status": "error",
                    "name": None,
                    "error": "541 - Rate Limited"
                }
        else:
            return {
                    "status": "error",
                    "name": None,
                    "error": f"HTTP {response.status_code}"
                }
    except Exception as e:
        return {
            "status": "error",
            "name": None,
            "error": f"Exception: {str(e)}"
        }


def sendDiscordMessage(message):
    response = requests.post(WEBHOOK_URL, json={"content": message})

def main():
    print(f"Starting monitor for store {storeNumber}, part {part_number}")
    sendDiscordMessage(f"🤖 Bot started monitoring {part_number} at store {storeNumber}")
    checkCount = 0

    lastStatus = "unavailable"

    while True:
        checkCount += 1
        currentTime = time.strftime('%I:%M:%S %p')
        result = checkSingleStore(part_number, storeNumber)

        if result["error"]:
            errorMessage = result["error"]
            message = f"❌ Check #{checkCount} (Error): {errorMessage}"
            sendDiscordMessage(message)

        else:
            currentStatus = result["status"]
            storeName = result["name"]

            #CHANGE NOTIFY TO BE IMPLEMENTED LATER
            # if currentStatus == "available" and lastStatus == "unavailable":
            #     message = f"{part_number} is available at {storeName}"
            #     sendDiscordMessage(message)
            #     lastStatus = "available"

            # elif currentStatus == "unavailable" and lastStatus == "available":
            #     message = f"{part_number} is no longer available at {storeName}"
            #     sendDiscordMessage(message)
            #     lastStatus = "unavailable"
            

            if currentStatus == "available":
                emoji = "🟢"
            else:
                emoji = "⚪"

            message = f"{emoji} Check #{checkCount}\n Time: {currentTime}\n{currentStatus} at {storeName}"
            sendDiscordMessage(message)

        time.sleep(600) #check every 10 minutes
        


if __name__ == "__main__":
    main()
# response = requests.get(storeUrl, timeout=10)
# print(f"Status: {response.status_code}")

# if response.status_code == 200:
#     data = response.json()
#     body = data["body"]


#     if "stores" in body: #making sure zip code is valid    
        
#         #SINGLE STORE LOGIC
#         #----------------------------------------
#         specificStore = body["stores"][0]

#         availability = specificStore["partsAvailability"][f"{part_number}/A"]["pickupDisplay"]

#         print(specificStore["storeName"])
#         print(availability)


#         #MULTIPLE STORE LOGIC
#         #---------------------------------------------------------
#         # for store in body["stores"]:
#         #     print(json.dumps(store, indent=2))
#         #     # print(store["storeName"], store["state"])

#         #     # partsAvailability = store["partsAvailability"] #digs through json to get availability
#         #     # modelInfo = partsAvailability[part_number + "/A"]
            
#         #     # print(modelInfo["pickupDisplay"]) #shows available or unavailable
#         #     # print(" ")        

#         # # firstStore = body["stores"][0]

#         # # if firstStore["state"] == "OR": #remove the hardcoding and change to softcoding later
#         # #     print(firstStore["storeName"])
#         # #     print("available")                #first store is 99 percent of the time an available store
            
#         # # else:
#         # #     print("unavailable")

    
#     else:
#         print("invalid zip code")


# elif response.status_code == 541:
#     print("541 error - likely rate limit or blocked. Wait 5-10 min, try VPN, or add more delays.")
# else:
#     print(f"Error: {response.status_code} - {response.text[:300]}")



