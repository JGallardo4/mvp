// Call the FedEx API to get the delivery date for a package
function getFedExDeliveryDate_(trackingNumber = "936780520280") {
  username = "valoredmonton";
  password = "Shipping1234";
  uniqueKey = "DNYRXOXH868NcqZJ";
  apiUrl = "https://ws.fedex.com:443/web-services";
  meterNumber = "253098545";

  var data = {
    version: 1,
    action: "trackpackages",
    locale: "en_US",
    format: "json",
    TrackPackagesRequest: {
      appType: "WTRK",
      appDeviceType: "DESKTOP",
      supportHTML: true,
      supportCurrentLocation: true,
      uniqueKey: uniqueKey,
      processingParameters: {},
      trackingInfoList: [
        {
          trackNumberInfo: {
            trackingNumber: trackingNumber,
            trackingQualifier: "",
            trackingCarrier: "",
          },
        },
      ],
    },
  };

  var options = {
    method: "post",
    contentType: "text/xml",
    payload: JSON.stringify(data),
  };

  data = UrlFetchApp.fetch(apiUrl, options).getContentText();
  Logger.log(data);

  // try {
  //   shipment = data.TrackResponse.Shipment;
  //   package = "";
  //   activity = "";
  //   status = "";
  //   date = "";

  //   if (shipment.Package.constructor === Array) {
  //     package = shipment.Package[0];
  //     Logger.log(shipment.Package[0]);
  //   } else {
  //     package = shipment.Package;
  //     Logger.log(shipment.Package.Activity);
  //   }

  //   if (package.Activity.constructor === Array) {
  //     activity = package.Activity[0];
  //   } else {
  //     activity = package.Activity;
  //   }

  //   status = activity.Status.Description;
  //   date = activity.Date;
  // } catch (error) {
  //   Logger.log(error)
  // }

  // if (status === "Delivered") {
  //   Logger.log(date)
  //   return date;
  // } else {
  //   Logger.log(status)
  //   Logger.log(date)
  //   return "null"
  // }
}
