import Vue from 'vue';
import Vuex from 'vuex';
import { isAuthTokenCookie } from '../helpers/commonHelpers';

Vue.use(Vuex);
console.log(isAuthTokenCookie);

export default new Vuex.Store({
  state: {
    auth: isAuthTokenCookie()
  },
  mutations: {
    switchAuth(state) {
      state.auth = !state.auth;
    }
  },
  actions: {},
  modules: {}
});
