import Vue from 'vue';
import VueRouter from 'vue-router';

import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Home from '../views/Home';
import store from '../store/index';

Vue.use(VueRouter);

const afterAuthGuard = (to, from, next) => {
  if (store.state.auth) {
    next('home');
  } else {
    next();
  }
};

const beforeAuthGuard = (to, from, next) => {
  if (store.state.auth) {
    next();
  } else {
    next('login');
  }
};

const routes = [
  {
    beforeEnter: afterAuthGuard,
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    beforeEnter: afterAuthGuard,
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    beforeEnter: beforeAuthGuard,
    path: '/home',
    name: 'home',
    component: Home,
    alias: '/'
  }
];

const router = new VueRouter({
  routes
});

export default router;
