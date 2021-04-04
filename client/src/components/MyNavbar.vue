<template>
  <nav>
    <ul class="navbar-list">
      <li>👤 {{ userName }}</li>

      <li>
        <button class="button" type="submit" value="Log out" @click="logout()">
          Logout
        </button>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "MyNavbar",
  computed: {
    userName: function () {
      return this.$store.getters.getUserName;
    },
  },
  methods: {
    logout: function () {
      this.$store.commit("DELETE_USERDATA");
      this.$router.push("/login-register");
    },
  },
};
</script>

<style lang="scss" scoped>
@use "../assets/css/variables" as *;
@use "../assets/css/mixins" as *;

.navbar-list {
  background-color: $light-green;
  color: $charcoal;
  padding: 1rem;
  display: flex;
  justify-content: right;
  align-items: center;
  gap: 1rem;
  @include mainFont();
}

.button {
  @include styleButton();
}

@media (max-width: 950px) {
  .navbar-list {
    justify-content: center;
  }
}
</style>
