<template>
  <div>
    <Notice v-if="afterRegMessage" v-bind:message="afterRegMessage" />
    <Errors v-bind:errors="errors" />
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
import { formatFormErrors } from '../helpers/commonHelpers';
import router from '../router/index';
import Errors from './Errors';
import Notice from './Notice';

export default {
  name: 'RegisterForm',
  components: { Notice, Errors },
  data() {
    return {
      email: '',
      username: '',
      password: '',
      passwordConfirmation: '',
      errors: [],
      afterRegMessage: ''
    };
  },
  methods: {
    tryRegister() {
      if (this.password !== this.passwordConfirmation) {
        this.errors = ['Password and password confirmation fields not equals'];
      } else {
        sendRegisterForm(this, {
          email: this.email,
          username: this.username,
          password: this.password
        });
      }
    },
    handleSuccessRegisterForm() {
      this.afterRegMessage = `your account will be available after
      confirmation by the administrator`;
      setTimeout(() => router.push('login'), 4000);
    },
    hadnleErrorRegisterForm(response) {
      this.errors = formatFormErrors(response.data);
    }
  }
};
</script>

<style scoped></style>
