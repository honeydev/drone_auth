<template>
  <div>
    <md-card>
      <md-card-media>
        <i class="material-icons userLogo">account_circle</i>
      </md-card-media>
      <md-card-header>
        <div class="md-title">{{ username }}</div>
      </md-card-header>
      <md-card-area class="md-layout md-alignment-center">
        <md-list class="md-double-line">
          <md-list-item>
            <md-icon class="md-primary">email</md-icon>

            <div class="md-list-item-text">
              <span>{{ email }}</span>
              <span>E-mail</span>
            </div>
          </md-list-item>
        </md-list>
      </md-card-area>
    </md-card>
  </div>
</template>

<script>
import { getUserProfile } from '../api/users';

export default {
  name: 'UserProfile',
  data: () => {
    return {
      username: null,
      email: null
    };
  },
  created() {
    getUserProfile(this);
  },
  methods: {
    successProfileData(response) {
      this.username = response.data.username;
      this.email = response.data.email;
    }
  }
};
</script>

<style scoped>
.userLogo {
  font-size: 100px;
}
</style>
