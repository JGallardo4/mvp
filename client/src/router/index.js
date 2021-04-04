import { createRouter, createWebHashHistory } from "vue-router";
import Track from "../views/Track.vue";
import LoginRegister from "../views/LoginRegister.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "Track",
    component: Track,
    beforeEnter: (to, from, next) => {
      if (store.getters.isLoggedIn) {
        next();
      } else {
        next("/login-register");
      }
    },
  },
  {
    path: "/login-register",
    name: "LoginRegister",
    component: LoginRegister,
    beforeEnter: (to, from, next) => {
      if (store.getters.isLoggedIn) {
        next("/");
      } else {
        next();
      }
    },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
