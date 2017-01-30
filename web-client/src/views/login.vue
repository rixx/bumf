<template>
  <form id="bumf-login">
    <bunt-input name="username" label="username" v-model="username" />
    <bunt-input name="password" label="password" type="password" v-model="password" />
    <bunt-button id="button-login" @click.native="login">
      Log in
    </bunt-button>
  </form>
</template>

<script>
import api from 'lib/api'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      api.login(this.username, this.password)
    },
  },
}
</script>

<style lang="stylus">
@import '~_settings'

#button-login
  button-style(color: $clr-danger)
</style>
