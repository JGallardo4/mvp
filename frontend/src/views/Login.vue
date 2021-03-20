<template>
  <body>
    <main>
      <div class="login-card">
        <form action="">
          <fieldset>
            <legend>Login</legend>

            <p>
              <label for="username">Username</label>
              <input type="text" name="email" v-model="input.username" />
            </p>

            <p>
              <label for="password">Password</label>
              <input type="password" name="password" v-model="input.password" />
            </p>

            <button @click.prevent="logIn()" id="submit-login">Log In</button>

            <p id="error-message" v-if="error">
              There was an error with your email and/or password.
            </p>
          </fieldset>

          <router-link to="/register">
            <p>Register</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
export default {
  name: "Login",

  data() {
    return {
      input: {
        username: "",
        password: "",
      },

      error: false,
    };
  },

  watch: {
    // Reset validation error when user begins typing new username
    "input.username": function() {
      this.error = false;
    },

    // Reset validation error when user begins typing new password
    "input.password": function() {
      if (this.input.password != "") {
        this.error = false;
      }
    },
  },

  methods: {
    logIn() {},
  },
};
</script>

<style lang="scss" scoped>
.login-card {
  border: solid 1px black;
}
</style>
