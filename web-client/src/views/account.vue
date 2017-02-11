<template>
  <div class="account" v-if="account">
    <div id="account-header">
      <span id="account-header-name">{{ account.name }}:</span>
      <span id="account-header-total" class="account-header-negative" v-if="account.total < 0">{{ account.total }} €</span>
      <span id="account-header-total" v-else>{{ account.total }} €</span>
    </div>
    <table id="transaction-table">
      <thead>
        <th>Date</th>
        <th>Payee</th>
        <th>Category</th>
        <th>Comment</th>
        <th>Inflow</th>
        <th>Outflow</th>
      </thead>
      <tbody>
        <template v-for="trans in transactions">
          <tr v-for="split in trans.transactions" @click="activeTransaction=(split == activeTransaction) ? null : split" :class="{active: split==activeTransaction}">
              <td class="transaction-date">{{ trans.timestamp | date }}</td>
              <td class="transaction-payee">{{ split.destination.name }}</td>
              <td class="transaction-category">{{ split.source.name }}</td>
              <td class="transaction-comment">{{ split.comment }}</td>
              <td class="transaction-in" v-if="trans.destination == account.id">{{ split.amount }} €</td>
              <td class="transaction-in" v-else></td>
              <td class="transaction-out" v-if="trans.source == account.id">{{ split.amount }} €</td>
              <td class="transaction-out" v-else></td>
          </tr>
        </template>
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
      activeTransaction: null,
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
  margin: 0
  table()

  tbody
    :hover
      background-color: $clr-grey-200
    .active, .active :hover
      background-color: $clr-cyan-500

  thead th, tbody td
    height: 0

  thead th
    background-color: $clr-cyan-100
    font-weight: normal
    padding: 16px

  tbody td
    border-color: $clr-grey-300
    border-bottom: border-separator()
    padding: 8px

  .transaction-date
    width: 80px

  .transaction-in, .transaction-out
    text-align: right
    width: 80px

</style>
