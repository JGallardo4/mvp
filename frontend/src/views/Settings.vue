<template>
  <body>
    <!-- <tweeter-header></tweeter-header> -->
    <main>
      <div>
        <form action="">
          <fieldset>
            <legend>Settings</legend>

            <p id="email-input">
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
            </p>

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

          <router-link to="track">
            <p>Track</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
export default {
  name: "Settings",

  data() {
    return {
      input: {
        email: "",
        username: "",
        bio: "",
        password: "",
      },

      error: false,
    };
  },

  watch: {
    "input.email": function() {
      this.error = false;
    },

    "input.password": function() {
      if (this.input.password != "") {
        this.error = false;
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
