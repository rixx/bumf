<template>
  <div class="account" v-if="account">
    {{ account.name }}
    <table>
      <thead></thead>
      <tbody>
        <tr v-for="transaction in transactions">
          <td>{{ transaction.amount }}</td>
          <td>{{ transaction.timestamp | date }}</td>
        </tr>
      </tbody>
    </table>
  </div>    
</template>

<script>
import api from 'lib/api'
export default {
  name: 'Account',
  components: {},
  props: ['id'],
  data () {
    return {
      account: null,
      transactions: [],
    }
  },
  computed: {},
  created () {
    this.fetchAccount()
  },
  watch: {
    // call again the method if the route changes
    '$route': 'fetchAccount'
  },
  mounted () {
    this.$nextTick(() => {
    })
  },
  methods: {
    fetchAccount () {
      api.realAccounts.get(this.$route.params.id).then((account) => {
        this.account = account
      })
      api.realTransactions.list(this.$route.params.id).then((transactions) => {
        this.transactions = transactions
      })
    }
  },
}
</script>

<style lang="stylus">
</style>
