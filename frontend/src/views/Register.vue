<template>
  <body>
    <main>
      <div>
        <form action="">
          <fieldset>
            <legend>Register</legend>

            <p>
              <label for="username">Username</label>
              <input
                type="text"
                name="username"
                v-model="input.username"
                placeholder=""
              />
            </p>

            <p>
              <label for="password">Password</label>
              <input
                type="password"
                name="password"
                v-model="input.password"
                placeholder=""
              />
            </p>

            <section>
              <button @click.prevent="register()">
                Register
              </button>
            </section>
          </fieldset>
          <router-link to="login">
            <p>Login</p>
          </router-link>
        </form>
      </div>
    </main>
  </body>
</template>

<script>
export default {
  name: "Register",

  data() {
    return {
      input: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    register() {},
  },
};
</script>

<style lang="scss" scoped></style>
