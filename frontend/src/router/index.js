import { createRouter, createWebHashHistory } from "vue-router";
import LuckyMain from "../views/LuckyMain.vue";

const routes = [
  {
    path: "/",
    name: "Main",
    component: LuckyMain,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
