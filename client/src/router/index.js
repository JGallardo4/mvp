import { createRouter, createWebHashHistory } from "vue-router";
import Track from "../views/Track.vue";

const routes = [
  {
    path: "/",
    name: "Track",
    component: Track,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
