from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from datetime import datetime


def get_tracking_info(fedex_api_key, password, account_number, meter_number, tracking_number):
    fedex_config = FedexConfig(key=fedex_api_key,
                               password=password,
                               account_number=account_number,
                               meter_number=meter_number)

    # Optional transaction_id
    customer_transaction_id = "*** TrackService Request v10 using Python ***"

    track = FedexTrackRequest(
        fedex_config, customer_transaction_id=customer_transaction_id)

    # Track by Tracking Number
    track.SelectionDetails.PackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'
    track.SelectionDetails.PackageIdentifier.Value = tracking_number

    del track.SelectionDetails.OperatingCompany

    track.send_request()

    for match in track.response.CompletedTrackDetails[0].TrackDetails:
        event_details = []
        if hasattr(match, 'DatesOrTimes'):
            for j in range(len(match.DatesOrTimes)):
                event_match = match.DatesOrTimes[j]
                event_details.append({'type': event_match.Type, 'date_time': event_match.DateOrTimestamp})

                if hasattr(event_match, 'StatusExceptionDescription'):
                    event_details[j]['exception_description'] = event_match.StatusExceptionDescription

    for item in event_details:
        if item["type"] == "ACTUAL_PICKUP":
            pickup_date = datetime.strptime(item["date_time"][0:10], "%Y-%m-%d")
        if item["type"] == "ACTUAL_DELIVERY":
            delivery_date = datetime.strptime(item["date_time"][0:10], "%Y-%m-%d")

    if not delivery_date:
        delivery_date: "In transit"

        return {
            "pickupDate": pickup_date,
            "deliveryDate": delivery_date,
            "deliveryTime": unavailable                
        }
    
    delivery_time = (delivery_date - pickup_date).days

    return {
        "delivery_date": delivery_date.date().strftime("%b %d, %Y"),
        "pickup_date": pickup_date.date().strftime("%b %d, %Y"),
        "deliveryTime": delivery_time
    }

# DatesOrTimes = {
#     (TrackingDateOrTimestamp){
#         Type = "ACTUAL_DELIVERY"
#         DateOrTimestamp = "2021-03-15T09:11:00-06:00"
#     },
#     (TrackingDateOrTimestamp){
#         Type = "ACTUAL_PICKUP"
#         DateOrTimestamp = "2021-03-12T14:43:00-07:00"
#     },
#     (TrackingDateOrTimestamp){
#         Type = "SHIP"
#         DateOrTimestamp = "2021-03-12T00:00:00"
#     },
#     (TrackingDateOrTimestamp){
#         Type = "ACTUAL_TENDER"
#         DateOrTimestamp = "2021-03-12T14:46:00-07:00"
#     }
# }

# fedex_response = {
#     HighestSeverity = "SUCCESS"

#     Notifications[] =
#     (Notification){
#         Severity = "SUCCESS"
#         Source = "trck"
#         Code = "0"
#         Message = "Request was successfully processed."
#         LocalizedMessage = "Request was successfully processed."
#     },

#     TransactionDetail =
#     (TransactionDetail){
#         CustomerTransactionId = "*** TrackService Request v10 using Python ***"
#     }

#     Version =
#     (VersionId){
#         ServiceId = "trck"
#         Major = 16
#         Intermediate = 0
#         Minor = 0
#     }

#     CompletedTrackDetails[] =

#     (CompletedTrackDetail){
#         HighestSeverity = "SUCCESS"
#         Notifications[] =
#         (Notification){
#             Severity = "SUCCESS"
#             Source = "trck"
#             Code = "0"
#             Message = "Request was successfully processed."
#             LocalizedMessage = "Request was successfully processed."
#         },

#         DuplicateWaybill = False
#         MoreData = False
#         TrackDetailsCount = 0
#         TrackDetails[] =

#         (TrackDetail){
#             Notification =
#             (Notification){
#                 Severity = "SUCCESS"
#                 Source = "trck"
#                 Code = "0"
#                 Message = "Request was successfully processed."
#                 LocalizedMessage = "Request was successfully processed."
#             }
#             TrackingNumber = "921547188999"
#             TrackingNumberUniqueIdentifier = "2459286000~921547188999~FX"
#             StatusDetail =
#             (TrackStatusDetail){
#                 CreationTime = 2021-03-15 00: 00: 00
#                 Code = "DL"
#                 Description = "Delivered"
#                 Location =
#                 (Address){
#                     City = "CALGARY"
#                     StateOrProvinceCode = "AB"
#                     CountryCode = "CA"
#                     CountryName = "Canada"
#                     Residential = False
#                 }
#             }
#             CarrierCode = "FDXE"
#             OperatingCompanyOrCarrierDescription = "FedEx Express"
#             Service =
#             (TrackServiceDescriptionDetail){
#                 Type = "FEDEX_EXPRESS_SAVER"
#                 Description = "FedEx Economy"
#                 ShortDescription = "XS"
#             }
#             PackageWeight =
#             (Weight){
#                 Units = "LB"
#                 Value = 7.0
#             }
#             PackageDimensions =
#             (Dimensions){
#                 Length = 12
#                 Width = 8
#                 Height = 5
#                 Units = "IN"
#             }
#             ShipmentWeight =
#             (Weight){
#                 Units = "LB"
#                 Value = 7.0
#             }
#             Packaging = "Your Packaging"
#             PackagingType = "YOUR_PACKAGING"
#             PackageSequenceNumber = 1
#             PackageCount = 1
#             CreatorSoftwareId = "CAFE"
#             SpecialHandlings[] =
#             (TrackSpecialHandling){
#                 Type = "DELIVER_WEEKDAY"
#                 Description = "Deliver Weekday"
#                 PaymentType = "OTHER"
#             },
#             (TrackSpecialHandling){
#                 Type = "RESIDENTIAL_DELIVERY"
#                 Description = "Residential Delivery"
#                 PaymentType = "OTHER"
#             },
#             Payments[] =
#             (TrackPayment){
#                 Classification = "TRANSPORTATION"
#                 Type = "SHIPPER_ACCOUNT"
#                 Description = "Shipper"
#             },
#             Shipper = ""
#             ShipperAddress =
#             (Address){
#                 City = "Edmonton"
#                 StateOrProvinceCode = "AB"
#                 CountryCode = "CA"
#                 CountryName = "Canada"
#                 Residential = False
#             }
#             DatesOrTimes[] =
#             (TrackingDateOrTimestamp){
#                 Type = "ACTUAL_DELIVERY"
#                 DateOrTimestamp = "2021-03-15T09:11:00-06:00"
#             },
#             (TrackingDateOrTimestamp){
#                 Type = "ACTUAL_PICKUP"
#                 DateOrTimestamp = "2021-03-12T14:43:00-07:00"
#             },
#             (TrackingDateOrTimestamp){
#                 Type = "SHIP"
#                 DateOrTimestamp = "2021-03-12T00:00:00"
#             },
#             (TrackingDateOrTimestamp){
#                 Type = "ACTUAL_TENDER"
#                 DateOrTimestamp = "2021-03-12T14:46:00-07:00"
#             },
#             Recipient = ""
#             DestinationAddress =
#             (Address){
#                 City = "CALGARY"
#                 StateOrProvinceCode = "AB"
#                 CountryCode = "CA"
#                 CountryName = "Canada"
#                 Residential = False
#             }
#             ActualDeliveryAddress =
#             (Address){
#                 City = "CALGARY"
#                 StateOrProvinceCode = "AB"
#                 CountryCode = "CA"
#                 CountryName = "Canada"
#                 Residential = False
#             }
#             DeliveryLocationType = "APARTMENT_OFFICE"
#             DeliveryLocationDescription = "Apartment Office"
#             DeliveryAttempts = 0
#             DeliverySignatureName = "J.FAUCHER"
#             TotalUniqueAddressCountInConsolidation = 0
#             AvailableImages[] =
#             (AvailableImagesDetail){
#                 Type = "SIGNATURE_PROOF_OF_DELIVERY"
#             },
#             NotificationEventsAvailable[] =
#             "ON_DELIVERY",
#             DeliveryOptionEligibilityDetails[] =
#             (DeliveryOptionEligibilityDetail){
#                 Option = "INDIRECT_SIGNATURE_RELEASE"
#                 Eligibility = "INELIGIBLE"
#             },
#             (DeliveryOptionEligibilityDetail){
#                 Option = "REDIRECT_TO_HOLD_AT_LOCATION"
#                 Eligibility = "INELIGIBLE"
#             },
#             (DeliveryOptionEligibilityDetail){
#                 Option = "REROUTE"
#                 Eligibility = "INELIGIBLE"
#             },
#             (DeliveryOptionEligibilityDetail){
#                 Option = "RESCHEDULE"
#                 Eligibility = "INELIGIBLE"
#             },
#             Events[] =
#             (TrackEvent){
#                 Timestamp = 2021-03-15 09: 11: 00-06: 00
#                 EventType = "DL"
#                 EventDescription = "Delivered"
#                 Address =
#                 (Address){
#                     City = "CALGARY"
#                     StateOrProvinceCode = "AB"
#                     PostalCode = "T2R1S2"
#                     CountryCode = "CA"
#                     CountryName = "Canada"
#                     Residential = False
#                 }
#                 ArrivalLocation = "DELIVERY_LOCATION"
#             },
#         },
#     },
# }
