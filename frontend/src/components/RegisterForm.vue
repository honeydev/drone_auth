<template>
  <div>
    <md-field>
      <label for="email">Email</label>
      <md-input v-model="email" id="email" type="email" name="email" />
    </md-field>
    <md-field md-clearable>
      <label for="username">Username</label>
      <md-input id="username" v-model="username"></md-input>
    </md-field>
    <md-field>
      <label for="password">Password</label>
      <md-input id="password" v-model="password" type="password"></md-input>
    </md-field>
    <md-field>
      <label for="passwordConfirmation">Password confirmation</label>
      <md-input
        id="passwordConfirmation"
        v-model="passwordConfirmation"
        type="password"
      ></md-input>
    </md-field>
    <md-button v-on:click="tryRegister" class="md-raised md-primary">
      Sign Up
    </md-button>
  </div>
</template>

<script>
import { sendRegisterForm } from '../api/auth';
import router from '../router/index';

export default {
  name: 'RegisterForm',
  data() {
    return {
      email: null,
      username: null,
      password: null,
      passwordConfirmation: null
    };
  },
  methods: {
    tryRegister() {
      sendRegisterForm(this, {
        email: this.email,
        username: this.username,
        password: this.password
      });
    },
    successRegisterForm() {
      router.push('login');
    }
  }
};
</script>

<style scoped></style>
