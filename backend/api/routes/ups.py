import secrets
from datetime import datetime

from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..clients import ups_client
from ..security.sec_utils import token_required, api_key_required

ups = Blueprint('/api/ups', __name__)

@ups.route("/api/ups", methods=["POST"])
@api_key_required
def get_delivery_time():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        access_license_number = data["accessLicenseNumber"]
        tracking_number = data["trackingNumber"]
        
        tracking_info = ups_client.getTrackingInfo(username, password, access_license_number, tracking_number)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Incorrect data"}), 400)
    else:        
        return make_response(jsonify(tracking_info), 201)