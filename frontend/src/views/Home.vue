<template>
  <div>
    <div class="md-layout md-gutter md-alignment-center">
      <div class="md-layout-item  md-size-35">
        <UserProfile />
      </div>
    </div>
  </div>
</template>

<script>
import UserProfile from '../components/UserProfile';

export default {
  name: 'Home',
  components: {
    UserProfile
  }
};
</script>
