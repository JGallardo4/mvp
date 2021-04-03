import { createRouter, createWebHashHistory } from "vue-router";
import Track from "../views/Track.vue";
import LoginRegister from "../views/LoginRegister.vue";
import Register from "../views/Register.vue";

const routes = [
  {
    path: "/",
    name: "Track",
    component: Track,
  },
  {
    path: "/login-register",
    name: "LoginRegister",
    component: LoginRegister,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
