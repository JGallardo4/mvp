<template>
  <body>
    <main>
      <p>Api</p>
    </main>
  </body>
</template>

<script>
export default {
  name: "Api",

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

<style lang="scss" scoped></style>
