<template>
  <div id="app">
    <div id="nav">
      <div v-if="!isAuth">
        <router-link to="/login">Sign in</router-link> |
        <router-link to="/register">Sign up</router-link>
      </div>
      <div v-else>
        <a href="#" v-on:click="logOut">Log out</a>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import router from './router/index';
// import Nav from './components/Nav';
import { removeAuthState } from './helpers/commonHelpers';

export default {
  created() {
    if (this.isAuth) {
      router.push('home');
    } else {
      router.push('login');
    }
  },
  computed: {
    isAuth() {
      return this.$store.state.auth;
    }
  },
  methods: {
    logOut() {
      removeAuthState(this.$store);
      router.push('login');
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #80bfff;
}
</style>
