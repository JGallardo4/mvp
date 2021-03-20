<template>
  <body>
    <!-- <tweeter-header></tweeter-header> -->
    <main>
      <div>
        <form action="">
          <fieldset>
            <legend>Track</legend>

            <p>
              <label for="carrier">Carrier</label>

              <select
                class="form-control"
                name="carrier"
                @change="changeCarrier($event)"
              >
                <option value="" selected disabled>Choose</option>

                <option
                  v-for="carrier in carriers"
                  :value="carrier.id"
                  :key="carrier.id"
                  >{{ carrier.name }}</option
                >
              </select>
            </p>

            <br /><br />

            <p>
              <span>Selected job title: {{ selectedCarrier }}</span>
            </p>

            <!-- <p id="email-input">
              <label for="email">Email</label>
              <input
                type="text"
                name="email"
                v-model="input.email"
                placeholder=""
              />
            </p>

            <p id="username-input">
              <label for="username">Username</label>
              <input
                type="text"
                name="username"
                v-model="input.username"
                placeholder=""
              />
            </p>

            <p id="password-input">
              <label for="password">Password</label>
              <input
                type="password"
                name="password"
                v-model="input.password"
                placeholder=""
              />
            </p> -->

            <section id="buttons">
              <button>
                Track
              </button>
            </section>

            <p id="error-message" v-if="error">
              There was an error with your email and/or password.
            </p>
          </fieldset>

          <router-link to="login">
            <p>Logout</p>
          </router-link>

          <router-link to="settings">
            <p>Settings</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
export default {
  name: "Track",

  data() {
    return {
      carriers: [
        { id: 1, name: "UPS" },
        { id: 2, name: "FedEx" },
        { id: 3, name: "Purolator" },
      ],

      selectedCarrier: null,
    };
  },

  methods: {
    changeCarrier(event) {
      this.selectedCarrier =
        event.target.options[event.target.options.selectedIndex].text;
    },
  },
};
</script>

<style lang="scss" scoped></style>
