<template>
  <header class="my-header">
    <section class="banner">
      <router-link to="/">
        <h1>
          Lucky
          <span class="clover">🍀</span>
          Tracker
        </h1>
      </router-link>
    </section>

    <my-navbar v-if="isLoggedIn"></my-navbar>
  </header>
</template>

<script>
import MyNavbar from "./MyNavbar.vue";

export default {
  name: "MyHeader",
  components: { MyNavbar },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn;
    },
  },
};
</script>

<style lang="scss" scoped>
@use "../assets/css/variables" as *;
@import url("https://fonts.googleapis.com/css2?family=Dela+Gothic+One&display=swap");

.my-header {
  text-align: center;
  padding-bottom: 3rem;
  padding-top: 1rem;
  background-color: $dark-green;
  color: white;

  .banner {
    font-family: "Dela Gothic One", cursive;
    font-size: x-large;
    padding-bottom: 1rem;
  }

  .clover {
    font-size: xx-large;
  }
}
</style>
