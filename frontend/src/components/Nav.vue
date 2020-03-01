<template>
  <div>
    <div v-if="!isAuth">
      <router-link to="/login">Sign in</router-link> |
      <router-link to="/about">Sign up</router-link>
    </div>
    <div v-else>
      <a href="/logout">Log out</a>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'Nav'
};
</script>

<style scoped></style>
