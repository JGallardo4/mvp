import json
from datetime import datetime
import requests
from config_secrets import secrets


def getTrackingInfo(username, password, access_license_number, tracking_number):
    url = "https://onlinetools.ups.com/json/Track"

    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": secrets["api"]["api-key"]
    }

    body = {
        u"Security": {
            u"UsernameToken": {
                u"Username": username,
                u"Password": password,
            },
            u"UPSServiceAccessToken": {
                u"AccessLicenseNumber": access_license_number,
            },
        },
        u"TrackRequest": {
            u"Request": {
                u"RequestAction": u"Track",
                u"RequestOption": u"activity",
            },
            u"InquiryNumber": tracking_number,
        },
    }

    try:
        response = requests.post(
            url=url, headers=headers, data=json.dumps(body)).json()
    except Exception as e:
        print("Error connecting to ups.com: ", e)

    if (not response.get("Fault")):
        shipment = response["TrackResponse"]["Shipment"]

        # Get pickup date
        pickup_date = datetime.strptime(shipment["PickupDate"], "%Y%m%d")

        if (type(shipment.get("Package")) == list):
            package = shipment["Package"][0]
        else:
            package = shipment["Package"]

        if (type(package["Activity"]) == list):
            activity = package["Activity"][0]
        else:
            activity = package["Activity"]        

        if (activity["Status"]["Description"] == "Delivered"):
            # Get delivery date
            delivery_date = datetime.strptime(activity["Date"], "%Y%m%d")

            #Get delivery time
            delivery_time = (delivery_date - pickup_date).days

            return { 
                "pickupDate": pickup_date.strftime("%a, %b %d %Y"), 
                "deliveryDate": delivery_date.strftime("%a, %b %d %Y"),
                "deliveryTime": delivery_time
            }
        else:
            return "In Transit"
    else:
        return "Error"