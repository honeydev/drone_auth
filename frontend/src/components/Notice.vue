<template>
  <div class="notice">
    <md-toolbar class="md-primary">
      <h3>{{ message }}</h3>
    </md-toolbar>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  props: {
    message: String
  }
};
</script>

<style scoped>
.notice {
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: #448aff;
  color: white;
}
</style>
