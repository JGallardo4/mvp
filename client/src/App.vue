<template>
  <my-header></my-header>
  <router-view />
</template>

<script>
import MyHeader from "./components/MyHeader.vue";
export default {
  components: { MyHeader },
};
</script>

<style lang="scss">
@use "./assets/css/variables" as *;

@import url("https://fonts.googleapis.com/css2?family=Lexend&display=swap");

main {
  padding: 1rem;
  color: white;
  background-color: $dark-green;
  min-height: 100vh;
  font-family: "Lexend", sans-serif;
}
</style>
