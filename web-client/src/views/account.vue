<template>
  <div class="account" v-if="account">
    <div id="account-header">
      <span id="account-header-name">{{ account.name }}:</span>
      <span id="account-header-total" class="account-header-negative" v-if="account.total < 0">{{ account.total }} €</span>
      <span id="account-header-total" v-else>{{ account.total }} €</span>
    </div>
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

.account
  width: 100%

#account-header
  width: 100%
  background-color: $clr-cyan-700
  padding: 8px

  #account-header-name
    color: $clr-white
    font-size: 18pt

  #account-header-total
    background-color: $clr-white
    border-radius: 8px
    font-size: 16pt
    font-weight: bold
    margin-left: 8px
    padding: 4px

#account-header-total.account-header-negative
  color: $clr-danger

#transaction-table
  display: table
  width: 100%

  tbody
    :hover
      background-color: $clr-grey-200

  tbody td, thead th
    border-collapse: collapse
    border-spacing: 0
    border-style: solid
    padding: 4px
    text-align: left

  thead th
    background-color: $clr-cyan-100
    border-width: 0
    font-weight: normal

  tbody td
    border-color: $clr-grey-300
    border-width: 0px 0px 1px 0px

  .transaction-date
    width: 80px

  .transaction-in, .transaction-out
    width: 80px
    text-align: right

</style>
