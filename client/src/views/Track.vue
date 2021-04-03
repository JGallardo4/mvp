<template>
  <main>
    <h1 class="page-title">Lucky Tracker</h1>

    <form class="form" @submit.prevent="track(carrier)">
      <div class="form-field">
        <label for="carrier">Carrier</label>
        <select id="carrier" v-model="carrier">
          <option value="">Select a carrier</option>
          <option
            v-for="(option, index) in carrierOptions"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </div>

      <template v-if="carrier == 'ups'">
        <div class="form-field">
          <label for="ups-username">UPS Username</label>
          <input id="ups-username" v-model="upsUserName" />
        </div>

        <div class="form-field">
          <label for="ups-access-license-number"
            >UPS Access License Number</label
          >
          <input
            id="ups-access-license-number"
            v-model="upsAccessLicenseNumber"
          />
        </div>

        <div class="form-field">
          <label for="ups-password">UPS Password</label>
          <input id="ups-password" v-model="upsPassword" />
        </div>

        <div class="form-field">
          <label for="ups-tracking-number">Tracking number</label>
          <input id="ups-tracking-number" v-model="upsTrackingNumber" />
        </div>
      </template>

      <template v-else-if="carrier == 'fedex'">
        <div class="form-field">
          <label for="fedex-api-key">FedEx API Key</label>
          <input id="fedex-api-key" v-model="fedexApiKey" />
        </div>

        <div class="form-field">
          <label for="fedex-account-number">FedEx Account Number</label>
          <input id="fedex-account-number" v-model="fedexAccountNumber" />
        </div>

        <div class="form-field">
          <label for="fedex-meter-number">FedEx Meter Number</label>
          <input id="fedex-meter-number" v-model="fedexMeterNumber" />
        </div>

        <div class="form-field">
          <label for="fedex-password">Fedex Password</label>
          <input id="fedex-password" v-model="fedexPassword" />
        </div>

        <div class="form-field">
          <label for="fedex-tracking-number">Tracking number</label>
          <input id="fedex-tracking-number" v-model="fedexTrackingNumber" />
        </div>
      </template>

      <template v-else-if="carrier == 'purolator'">
        <p>This feature is not available right now.</p>
        <p>
          Please visit
          <a href="https://www.purolator.com/en/shipping/tracker"
            >Purolator.com</a
          >
          to track your package.
        </p>
      </template>

      <template v-if="carrier !== '' && carrier !== 'purolator'">
        <div class="form-field">
          <label for="lucky-tracker-api-key">Lucky Tracker API Key</label>
          <input id="lucky-tracker-api-key" v-model="luckyTrackerApiKey" />
        </div>

        <button
          class="form-button"
          type="submit"
          value="Get delivery time."
          @click="clearResult()"
        >
          Get Delivery Time
        </button>
      </template>

      <template v-else-if="carrier === ''">
        <p>Please select a carrier.</p>
      </template>
    </form>

    <div v-if="result !== ''">
      <p>Carrier: {{ resultShipment["carrier"] }}</p>
      <p>Tracking number: {{ resultShipment["trackingNumber"] }}</p>
      <p>Pickup date: {{ result.pickupDate }}</p>
      <p>
        Delivery date:
        {{ result.deliveryDate }}
      </p>
      <p>Delivery time: {{ result.deliveryTime }}</p>

      <button
        class="form-button"
        type="submit"
        value="Clear result"
        @click="clearResult()"
      >
        Clear result
      </button>
    </div>
  </main>
</template>

<script>
export default {
  name: "Track",

  data() {
    return {
      carrier: "",
      carrierOptions: [
        { text: "UPS", value: "ups" },
        { text: "FedEx", value: "fedex" },
        { text: "Purolator", value: "purolator" },
      ],
      trackingNumber: "",
      upsUserName: "",
      upsAccessLicenseNumber: "",
      upsPassword: "",
      upsTrackingNumber: "",
      fedexApiKey: "",
      fedexAccountNumber: "",
      fedexMeterNumber: "",
      fedexPassword: "",
      luckyTrackerApiKey: "",
      fedexTrackingNumber: "",
      result: "",
      resultShipment: {
        carrier: "",
        trackingNumber: "",
      },
    };
  },

  methods: {
    clearResult: function () {
      this.result = "";
      this.resultShipment = null;
    },

    track: function (carrier) {
      var payload = null;

      // var baseUrl = "https://luckytracker.tk/api";

      if (carrier === "ups") {
        payload = {
          username: this.upsUserName,
          password: this.upsPassword,
          accessLicenseNumber: this.upsAccessLicenseNumber,
          trackingNumber: this.upsTrackingNumber,
        };

        this.axios
          .post("/ups", payload, {
            headers: {
              "X-Api-Key": this.luckyTrackerApiKey,
            },
          })
          .then((response) => {
            if (response.status === 201) {
              this.result = response.data;
              this.resultShipment = {
                carrier: "UPS",
                trackingNumber: this.upsTrackingNumber,
              };
            } else {
              console.log("failure");
            }
          })
          .catch((error) => {
            console.log(error);
          });
      } else if (carrier == "fedex") {
        payload = {
          fedexApiKey: this.fedexApiKey,
          password: this.fedexPassword,
          accountNumber: this.fedexAccountNumber,
          meterNumber: this.fedexMeterNumber,
          trackingNumber: this.fedexTrackingNumber,
        };

        this.axios
          .post("/fedex", payload, {
            headers: {
              "X-Api-Key": this.luckyTrackerApiKey,
            },
          })
          .then((response) => {
            if (response.status === 200) {
              this.result = response.data;
              this.resultShipment = {
                carrier: "FedEx",
                trackingNumber: this.fedexTrackingNumber,
              };
            } else {
              console.log("failure");
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
main {
  padding: 1rem;
}

.page-title {
  font-size: x-large;
  text-align: center;
}

.form {
  display: grid;

  .form-field {
    display: flex;
    flex-direction: column;
    padding: 1rem;

    label {
      padding-bottom: 0.5rem;
    }
  }

  .form-button {
    place-self: center;
  }
}
</style>
