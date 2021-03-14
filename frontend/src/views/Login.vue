<template>
  <div class="container">
    <div>
      <button class="btn btn-success">Login As Guest</button>
      <button class="btn btn-success">Register</button>
      <button class="btn btn-success">Login</button>
    </div>
    <div v-if="loginType == 0" class="form-group card">
      <label>
        <label>Guest Name: </label>
        <input type="text" v-model="userObj.userName" />
      </label>
      <button class="btn btn-success" v-on:click="login()">
        Login As Guest
      </button>
    </div>
  </div>
</template>

<script>
import store from "@/store";
export default {
  data() {
    return {
      loginType: 0,
      userObj: {
          userName:null,
          password:null
      },
    };
  },
  methods: {
    login() {
        this.userObj['loginType'] = this.loginType;
      store
        .dispatch("login/userLogin", this.userObj)
        .then(() => {
          console.log("Login Successfull");
          this.$router.push({
              name: "ChatView"
            });
        })
        .catch((err) => {
          console.log(err);
          this.$toasted.show(err).goAway(1500)
        });
    },
  },
};
</script>

<style></style>
