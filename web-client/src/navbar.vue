<template>
  <div id="navbar">
    <div id="nav-account-links">
      <router-link :to="{ name: 'budget'}">Budget</router-link>
      <router-link v-for="account in accounts" :to="{ name: 'account', params: {id: account.id}}">
        <div class="nav-account-name">{{ account.name }}</div>
        <div class="nav-account-amount nav-account-amount-negative" v-if="account.total < 0">{{ account.total }} €</div>
        <div class="nav-account-amount" v-else>{{ account.total }} €</div>
      </router-link>
    </div>
    <div id="nav-user-links">
      <bunt-button id="nav-username">{{ username }}</bunt-button>
      <bunt-button id="nav-logout" @click.native="performLogout">logout</bunt-button>
  </div>
</template>

<script>
import api from 'lib/api'
import auth from 'lib/auth'

export default {
  data () {
    return {
      accounts: [],
      username: auth.authUser,
    }
  },
  mounted () {
    api.realAccounts.list().then((list) => {
      this.accounts = list
    })
  },
  methods: {
    performLogout () {
      api.logout()
      this.$router.push({ path: '/login' })
    }
  }
}
</script>

<style lang="stylus">
@import '~_settings'

#navbar
  background-color: $clr-primary
  display: flex
  flex-direction: column
  flex-shrink: 0
  justify-content: space-between
  padding: 16px
  width: 240px

#nav-account-links
  display: flex
  flex-direction: column
  padding-top: 240px

  :hover
    background-color: $clr-primary-dark

#nav-user-links
  align-items: baseline
  display: flex
  flix-direction: row
  justify-content: space-between

  #nav-username
    background-color: $clr-primary-dark

#nav-account-links .router-link-active
  background-color: $clr-primary-active

  :hover
    background-color: $clr-primary-active

#nav-account-links a
  display: flex
  flex-direction: row
  justify-content: space-between
  color: $clr-black
  padding: 8px
  text-decoration: none

.nav-account-amount
  font-weight: bold
  padding: 1px 1px 2px 1px

.nav-account-amount-negative
  background-color: $clr-white
  border-radius: 4px
  color: $clr-danger

</style>
