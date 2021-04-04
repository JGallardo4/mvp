import { createStore } from "vuex";
import VuexPersistence from "vuex-persist";

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

export default createStore({
  state: {
    user: {
      userId: "",
      userName: "",
      loginToken: "",
    },
  },

  getters: {
    getUser(state) {
      return state.user;
    },

    getUserName(state) {
      return state.user["userName"];
    },

    getUserId(state) {
      return state.user["userId"];
    },

    getLoginToken(state) {
      return state.user["loginToken"];
    },

    isLoggedIn(state) {
      return state.user["loginToken"] !== "";
    },
  },

  mutations: {
    SET_USER(state, payload) {
      state.user = payload;
    },

    DELETE_USERDATA(state) {
      state.user = {
        userId: "",
        userName: "",
        loginToken: "",
      };
    },
  },
  plugins: [vuexLocal.plugin],
});
