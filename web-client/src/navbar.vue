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
