<template>
  <div>
    <div class="md-layout md-gutter md-alignment-center">
      <div class="md-layout-item  md-size-30">
        <LoginForm />
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm';

export default {
  name: 'Login',
  components: {
    LoginForm
  }
};
</script>
