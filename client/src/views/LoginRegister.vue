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
          <input id="user-name" v-model="userInfo.username" />
        </div>

        <div class="form-field">
          <label for="password">Password</label>
          <input id="password" v-model="userInfo.password" type="password" />
        </div>

        <div class="form-field">
          <label for="lucky-tracker-api-key">Lucky Tracker API Key</label>
          <input
            id="lucky-tracker-api-key"
            v-model="luckyTrackerApiKey"
            type="password"
          />
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
        username: "",
        password: "",
      },
      luckyTrackerApiKey: "",
    };
  },

  computed: {
    actionLabel: function () {
      return this.mode === "login" ? "Log in" : "Register";
    },
  },

  methods: {
    action: function (userInfo) {
      if (this.mode === "login") {
        return this.login(userInfo);
      } else if (this.mode === "register") {
        return this.register(userInfo);
      }
    },

    login(userInfo) {
      this.axios
        .post("/login", userInfo, {
          headers: {
            "X-Api-Key": this.luckyTrackerApiKey,
          },
        })
        .then((response) => {
          if (response.status === 201) {
            var responseData = response.data[0];

            this.$store.commit("SET_USER", {
              userId: responseData["Id"],
              userName: responseData["Username"],
              loginToken: responseData["loginToken"],
            });

            this.$router.push("/");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    register(userInfo) {
      this.axios
        .post("/users", userInfo, {
          headers: {
            "X-Api-Key": this.luckyTrackerApiKey,
          },
        })
        .then((response) => {
          if (response.status === 201) {
            var responseData = response.data[0];

            this.$store.commit("SET_USER", {
              userId: responseData["Id"],
              userName: responseData["Username"],
              loginToken: responseData["loginToken"],
            });

            this.$router.push("/");
          }
        })
        .catch((error) => {
          console.log(error);
        });
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
