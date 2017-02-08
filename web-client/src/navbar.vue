<template>
  <div id="navbar">
    <router-link :to="{ name: 'budget'}">Budget</router-link>
    <router-link v-for="account in accounts" :to="{ name: 'account', params: {id: account.id}}">{{ account.name }}</router-link>
  </div>
</template>

<script>
import api from 'lib/api'
export default {
  data () {
    return {
      accounts: [],
    }
  },
  mounted () {
    api.realAccounts.list().then((list) => {
      this.accounts = list
    })
  }
}
</script>

<style lang="stylus">
@import '~_settings'

#navbar
  background-color: $clr-primary
  display: flex
  flex-direction: column
  width: 240px
  padding: 16px
</style>
