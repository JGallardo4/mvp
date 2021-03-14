// Call the UPS API to get the delivery date for a package
function getUpsDeliveryDate_(trackingNumber) {
  username = "EdmontonValor";
  password = "V@lorDistributions1";
  accessLicenseNumber = "1D954279433E51B2";
  apiUrl = "https://onlinetools.ups.com/json/Track";

  var data = {
    Security: {
      UsernameToken: {
        Username: username,
        Password: password,
      },
      UPSServiceAccessToken: {
        AccessLicenseNumber: accessLicenseNumber,
      },
    },
    TrackRequest: {
      Request: {
        RequestAction: "Track",
        RequestOption: "activity",
      },
      InquiryNumber: trackingNumber,
    },
  };

  var options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(data),
  };

  package = "";
  activity = "";
  status = "No updates";
  date = "In transit";

  try {
    data = JSON.parse(UrlFetchApp.fetch(apiUrl, options).getContentText());

    if (!data.Fault) {
      shipment = data.TrackResponse.Shipment;

      if (shipment.Package.constructor === Array) {
        package = shipment.Package[0];
      } else {
        package = shipment.Package;
      }

      if (package.Activity.constructor === Array) {
        activity = package.Activity[0];
      } else {
        activity = package.Activity;
      }

      status = activity.Status.Description;
      date = activity.Date;
    }
  } catch (error) {
    Logger.log(error);
  }

  if (status === "Delivered") {
    dateStr = date.slice(0, 4) + "-" + date.slice(4);
    dateStr = dateStr.slice(0, 7) + "-" + dateStr.slice(7);
    // options = { year: 'numeric', month: 'numeric', day: 'numeric' };
    // formattedDate = new Date(dateStr).toLocaleDateString('en-US', options);

    date = new Date(dateStr);
    return date;
  } else {
    return "In Transit";
  }
}
