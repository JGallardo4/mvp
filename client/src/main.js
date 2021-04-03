import { createApp } from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";

axios.defaults.headers.common["X-Api-Key"] =
  "1Rj5dMCW6aOfA75kbtKt6Gcatc5M9Chc6IGwJKe4YdhDD";

axios.defaults.headers.common["Content-Type"] = "application/json";

axios.defaults.baseURL = "https://luckytracker.tk/api";

// Log user out when token expires
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      console.log("invalid token!");
      store.dispatch("logOut");
      return Promise.reject(error);
    } else {
      throw error;
    }
  }
);

createApp(App).use(store).use(router).mount("#app");
