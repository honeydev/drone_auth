<template>
  <div v-if="errors.length">
    <md-toolbar class="md-accent errors">
      <ul>
        <li v-bind:key="error" v-for="error in errors">{{ error }}</li>
      </ul>
    </md-toolbar>
  </div>
</template>

<script>
export default {
  name: 'Errors',
  props: {
    errors: Array
  }
};
</script>

<style scoped>
.errors {
  background-color: rgb(255, 82, 82);
  color: white;
}
</style>
