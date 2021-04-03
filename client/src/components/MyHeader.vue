<template>
  <header class="my-header">
    <router-link to="/">
      <h1>
        Lucky
        <span class="clover">🍀</span>
        Tracker
      </h1></router-link
    >
  </header>
</template>

<script>
export default {
  name: "MyHeader",
};
</script>

<style lang="scss" scoped>
@use "../assets/css/variables" as *;

.my-header {
  font-size: x-large;
  text-align: center;
  padding-bottom: 3rem;
  padding-top: 1rem;
  font-family: "Dela Gothic One", cursive;
  background-color: $dark-green;
  color: white;

  .clover {
    font-size: xx-large;
  }
}
</style>
