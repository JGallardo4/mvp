import { createApp } from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/css/main.scss";

axios.defaults.headers.common["Content-Type"] = "application/json";

axios.defaults.baseURL = "https://luckytracker.tk/api";

createApp(App).use(VueAxios, axios).use(store).use(router).mount("#app");
