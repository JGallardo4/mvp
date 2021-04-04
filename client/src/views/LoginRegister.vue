<template>
  <main>
    <form class="form" @submit.prevent="action(userInfo)">
      <div class="form-field">
        <label for="mode">Login / Register</label>
        <select id="mode" v-model="mode">
          <option value="">Select either</option>
          <option
            v-for="(option, index) in modeOptions"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </div>
      <template v-if="mode !== ''">
        <div class="form-field">
          <label for="user-name">Username</label>
          <input id="user-name" v-model="userInfo.userName" />
        </div>

        <div class="form-field">
          <label for="password">Password</label>
          <input id="password" v-model="userInfo.password" type="password" />
        </div>

        <button class="form-button" type="submit" value="Get delivery time.">
          {{ actionLabel }}
        </button>
      </template>
    </form>
  </main>
</template>

<script>
export default {
  name: "LoginRegister",

  data() {
    return {
      mode: "",
      modeOptions: [
        { text: "Login", value: "login" },
        { text: "Register", value: "register" },
      ],
      userInfo: {
        userName: "",
        password: "",
      },
    };
  },

  computed: {
    actionLabel: function () {
      return this.mode === "login" ? "Log in" : "Register";
    },
  },

  methods: {
    login: function (userInfo) {
      this.$store.commit("SET_USER", {
        userId: "1",
        userName: userInfo.userName,
        loginToken: "myLoginToken123",
      });

      this.$router.push("/");
    },

    register: function (userInfo) {
      this.$store.commit("SET_USER", {
        user: userInfo.userName,
        loginToken: "myLoginToken123",
      });
    },

    action: function (userInfo) {
      if (this.mode === "login") {
        return this.login(userInfo);
      } else if (this.mode === "register") {
        return this.register(userInfo);
      }
    },
  },
};
</script>

<style lang="scss">
@use "../assets/css/mixins" as *;

.form {
  @include styleForm();
}
</style>
