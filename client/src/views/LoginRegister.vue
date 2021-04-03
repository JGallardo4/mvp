<template>
  <main>
    <form class="form" @submit.prevent="track(carrier)">
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
          <input id="user-name" v-model="userName" />
        </div>

        <div class="form-field">
          <label for="password">Password</label>
          <input id="password" v-model="password" type="password" />
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
      userName: "",
      password: "",
    };
  },

  computed: {
    actionLabel: function () {
      return this.mode === "login" ? "Log in" : "Register";
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
