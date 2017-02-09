<template>
  <div class="account" v-if="account">
    {{ account.name }}
    <table id="transaction-table">
      <thead>
        <th class="transaction-date">Date</th>
        <th class="transaction-payee">Payee</th>
        <th class="transaction-category">Category</th>
        <th class="transaction-comment">Comment</th>
        <th class="transaction-in">Inflow</th>
        <th class="transaction-out">Outflow</th>
      </thead>
      <tbody>
        <tr v-for="transaction in transactions">
          <td class="transaction-date">{{ transaction.timestamp | date }}</td>
          <td class="transaction-payee"></td>
          <td class="transaction-category"></td>
          <td class="transaction-comment"></td>
          <td class="transaction-in" v-if="transaction.destination == account.id">{{ transaction.amount }}</td>
          <td class="transaction-in" v-else></td>
          <td class="transaction-out" v-if="transaction.source == account.id">{{ transaction.amount }}</td>
          <td class="transaction-out" v-else></td>
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

#transaction-table
  display: table

  tbody td, thead th
    text-align: left
    border-collapse: collapse
    border-style: solid

  thead th
    border-color: $clr-primary
    border-width: 2px 0px 2px 0px

  tbody td
    border-width: 0px 0px 2px 0px
    border-color: $clr-inactive

  .transaction-date
    width: 20%
  .transaction-payee, .transaction-category
    width: 10%
  .transaction-in, .transaction-out
    text-align: right
    width: 10%
  .transaction-comment
    width: 20%

</style>
