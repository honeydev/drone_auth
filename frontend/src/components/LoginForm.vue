<template>
  <div>
    <Errors v-bind:errors="errors" />
    <md-field md-clearable>
      <label>Username</label>
      <md-input v-model="username"></md-input>
    </md-field>
    <md-field>
      <label>Password</label>
      <md-input v-model="password" type="password"></md-input>
    </md-field>
    <md-button v-on:click="tryLogin" class="md-raised md-primary">
      Sign in
    </md-button>
  </div>
</template>

<script>
import { sendLoginForm } from '../api/auth';
import router from '../router/index';
import { setAuntState, formatFormErrors } from '../helpers/commonHelpers';
import Errors from './Errors';

export default {
  components: {
    Errors
  },
  data() {
    return {
      username: null,
      password: null,
      errors: []
    };
  },
  name: 'LoginForm',
  methods: {
    tryLogin() {
      sendLoginForm(this, {
        username: this.username,
        password: this.password
      });
    },
    successLoginForm(response) {
      setAuntState(
        {
          access: response.data.access,
          refresh: response.data.refresh
        },
        this.$store
      );
      router.push('home');
    },
    errorLoginForm(response) {
      this.errors = formatFormErrors(response.data);
    }
  }
};
</script>
