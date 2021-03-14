/**
 * Returns the amount of days elapsed between the shipping date and the delivery date.
 * If a full day has not passed, the result is zero. Otherwise returns the days rounded up from 0.5
 * Returns an empty string if the delivery date is not available
 *
 * @param {string} trackingNumber Tracking number of the shipment
 * @param {string} carrier Carrier, from "UPS", "FedEx", or "PURO"
 * @param {string} shippingDateString Date of shipment with format "12/30/9999"
 *
 * @return {string} Delivery time
 */
function getDeliveryTime(trackingNumber, carrier, shippingDateString) {
  var shippingDate = new Date(shippingDateString);
  var deliveryDate = getDeliveryDate(carrier, trackingNumber);

  if (carrier !== "UPS") {
    return "Carrier not available yet";
  }

  console.log("Shipping date: " + shippingDate);
  console.log("Delivery date: " + deliveryDate);

  if (deliveryDate !== "In Transit" || deliveryDate === "") {
    var span = Math.round(
      Math.abs((deliveryDate - shippingDate) / (1000 * 60 * 60 * 24))
    );
    console.log(span);
    return span;
  } else {
    return "In Transit";
  }
}

function getDeliveryDate(carrier, trackingNumber) {
  var deliveryDate = "";

  if (carrier === "UPS") {
    deliveryDate = getUpsDeliveryDate(trackingNumber);
  } else if (carrier === "FedEx") {
    // deliveryDate = getFedExDeliveryDate(trackingNumber); // Not implemented yet
  } else if (carrier === "PURO") {
    // deliveryDate = getPuroDeliveryDate(trackingNumber); // Not implemented yet
  }

  return deliveryDate;
}

getDeliveryTime("1Z0204512046234654", "UPS", "03/08/2021");
