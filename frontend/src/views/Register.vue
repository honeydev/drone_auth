<template>
  <div class="md-layout md-gutter md-alignment-center">
    <div class="md-layout-item  md-size-30">
      <RegisterForm />
    </div>
  </div>
</template>

<script>
import RegisterForm from '../components/RegisterForm';

export default {
  name: 'Register',
  components: { RegisterForm },
  comments: {
    RegisterForm
  }
};
</script>
