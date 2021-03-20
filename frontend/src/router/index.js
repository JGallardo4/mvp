import { createRouter, createWebHashHistory } from "vue-router";
import LuckyMain from "../views/LuckyMain.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Track from "../views/Track.vue";
import Settings from "../views/Settings.vue";
import Api from "../views/Api.vue";

const routes = [
  {
    path: "/",
    name: "Main",
    component: LuckyMain,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/track",
    name: "Track",
    component: Track,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
  },
  {
    path: "/api",
    name: "Api",
    component: Api,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
