<template>
  <div>
    <form class="track" @submit.prevent="track">
      <h1>Track</h1>

      <label>Carrier</label>
      <select v-model="selected">
        <option disabled value="">Select a carrier</option>
        <option
          v-for="(option, index) in options"
          :value="option.value"
          :key="index"
        >
          {{ option.text }}
        </option>
      </select>

      <label>Password</label>
      <input
        required
        v-model="password"
        type="password"
        placeholder="Password"
      />

      <button type="submit">Track</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Track",
  methods: {
    track: function () {},
  },
  data() {
    return {
      selected: "",
      options: [
        { text: "UPS", value: "ups" },
        { text: "FedEx", value: "fedex" },
        { text: "Purolator", value: "purolator" },
      ],
    };
  },
};
</script>

<style>
/* @import "vue-select/src/scss/vue-select.scss"; */
</style>
