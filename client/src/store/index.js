import { createStore } from "vuex";
import axios from "axios";
import router from "../router/index.js";

export default createStore({
  state: {
    userId: "",
    userName: "",
    loginToken: "",
  },

  getters: {
    getUserName(state) {
      return state.userName;
    },

    getUserId(state) {
      return state.userId;
    },

    getLoginToken(state) {
      return state.loginToken;
    },
  },

  mutations: {
    SET_USERID(state, payload) {
      state.userId = payload;
    },

    SET_LOGIN_TOKEN(state, payload) {
      state.loginToken = String(payload);
    },

    SET_USERNAME(state, payload) {
      state.userName = payload;
    },

    DELETE_USERDATA(state) {
      state.userId = "";
      state.userName = "";
      state.loginToken = "";
    },
  },

  actions: {
    logIn({ commit }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/login", payload)
          .then((response) => {
            if (response.status === 201) {
              var _user = response.data[0];
              commit("SET_LOGIN_TOKEN", _user.loginToken);
              commit("SET_USERID", _user.userId);
              commit("SET_USERNAME", _user.username);
              resolve(response);
            } else {
              reject(response);
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    },

    logOut({ commit, dispatch }) {
      commit("DELETE_USERDATA");
      dispatch("redirect", "/login");
    },

    checkLogin({ dispatch }) {
      if (this.getters.getLoginToken !== "") {
        dispatch("redirect", "/");
      } else {
        dispatch("logOut");
      }
    },

    register({ dispatch }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .post("/users", payload)
          .then((response) => {
            if (response.status === 201) {
              dispatch("logIn", {
                email: payload["email"],
                password: payload["password"],
              });
              dispatch("redirect", "/");
              resolve(response);
            } else {
              reject(response);
            }
          })
          .catch((error) => {
            reject(error);
          });
      });
    },

    initializeStore({ state }) {
      if (window.localStorage.getItem("vuex")) {
        this.replaceState(
          Object.assign(state, JSON.parse(window.localStorage.getItem("state")))
        );
      }
    },

    deleteAccount({ dispatch }, payload) {
      return new Promise((resolve, reject) => {
        axios
          .delete("/users", { data: payload })
          .then((response) => {
            if (response.status === 204) {
              resolve(response);
              dispatch("logOut");
            }
          })
          .catch((error) => reject(error.response));
      });
    },

    getUser(state, payload) {
      return axios
        .get("/users", { params: { userId: payload } })
        .catch((error) => {
          console.log(error);
        });
    },

    redirect(state, route) {
      if (router.currentRoute !== route) {
        router.push(route).catch((error) => {
          if (
            error.name !== "NavigationDuplicated" &&
            !error.message.includes(
              "Avoided redundant navigation to current location"
            )
          ) {
            console.log(error);
          }
        });
      }
    },
  },
});
