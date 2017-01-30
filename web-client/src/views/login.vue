<template>
  <div id="bumf">
    <div id="exposition">
      <h2>welcome!</h2>
      bumf is a budgeting tool - it is open source, ready to be self-hosted and
      is ready to help you keep your finances in order!
    </div>
    <div id="form-container">
      <form class="bumf-userform" id="bumf-register">
        <bunt-input name="username" label="username" v-model="register.username" />
        <bunt-input name="password" label="password (highly secret!)" type="password" v-model="register.password" />
        <bunt-input name="firstname" label="What should we call you? (optional)" v-model="register.firstname" />
        <bunt-input name="email" label="How can we reach you? (optional)" v-model="register.email" />
        <bunt-button id="button-register" class="bumf-userbutton" @click.native="performRegister">
          register
        </bunt-button>
      </form>
      <form class="bumf-userform" id="bumf-login">
        <bunt-input name="username" label="username" v-model="login.username" />
        <bunt-input name="password" label="password" type="password" v-model="login.password" />
        <bunt-button id="button-login" class="bumf-userbutton" @click.native="performLogin">
          log in
        </bunt-button>
      </form>
    </div>
  </div>
</template>

<script>
import api from 'lib/api'

export default {
  data () {
    return {
      login: {
        username: '',
        password: ''
      },
      register: {
        username: '',
        password: '',
        firstname: '',
        email: ''
      }
    }
  },
  methods: {
    performLogin () {
      api.login(this.login.username, this.login.password).then(() => {
        this.$router.push({ path: '/' })
      })
    },
    performRegister () {
        api.register(this.register.username, this.register.password, this.register.firstname, this.register.email).then(() => {
        this.$router.push({ path: '/' })
      })
    },
  },
}
</script>

<style lang="stylus">
@import '~_settings'

#button-login
  button-style(color: $clr-danger)
</style>
