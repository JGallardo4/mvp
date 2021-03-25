import secrets
from datetime import datetime

from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..clients import fedex_client
from ..security.sec_utils import token_required, api_key_required

fedex = Blueprint('/api/fedex', __name__)

@fedex.route("/api/fedex", methods=["POST"])
@api_key_required
def get_tracking_info():    
    try:
        data = request.get_json()
        fedex_api_key = data["fedexApiKey"]
        password = data["password"]
        account_number = data["accountNumber"]
        meter_number = data["meterNumber"]
        tracking_number = data["trackingNumber"]
        
        tracking_info = fedex_client.get_tracking_info(
            fedex_api_key=fedex_api_key, password=password, account_number=account_number, meter_number=meter_number, tracking_number=tracking_number) 
    except Exception as e:
        print(e)
        return "", 500
    else:
        return make_response(jsonify(tracking_info), 200)
