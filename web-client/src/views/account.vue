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
      <tbody class="transaction-new">
        <tr class="transaction-input">
          <td class="transaction-date"><bunt-input v-model="newTransaction.date" name="newTransactionDate"></bunt-input></td>
          <td class="transaction-payee"><bunt-input v-model="newTransaction.payee" name="newTransactionPayee"></bunt-input></td>
          <td class="transaction-category"><bunt-input v-model="newTransaction.category" name="newTransactionCategory"></bunt-input></td>
          <td class="transaction-comment"><bunt-input v-model="newTransaction.comment" name="newTransactionComment"></bunt-input></td>
          <td class="transaction-in"><bunt-input v-model="newTransaction.inflow" name="newTransactionIn"></bunt-input></td>
          <td class="transaction-out"><bunt-input v-model="newTransaction.outflow" name="newTransactionOut"></bunt-input></td>
        </tr>
        <tr class="transaction-confirm">
          <td colspan="6"><bunt-button @click.native="performCreate">Save</bunt-button></td>
        </tr>
      </tbody>
      <tbody class="transaction-list">
        <template v-for="trans in transactions">
          <tr v-for="split in trans.transactions" @click="activeTransaction=(split === activeTransaction) ? null : split" :class="{active: split === activeTransaction}">
            <td class="transaction-date">{{ trans.timestamp | date }}</td>
            <td class="transaction-payee">{{ split.destination.name }}</td>
            <td class="transaction-category">{{ split.source.name }}</td>
            <td class="transaction-comment">{{ split.comment }}</td>
            <td class="transaction-in" v-if="trans.destination === account.id">{{ split.amount }} €</td>
            <td class="transaction-in" v-else></td>
            <td class="transaction-out" v-if="trans.source === account.id">{{ split.amount }} €</td>
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
      newTransaction: {
        date: '',
        payee: '',
        category: '',
        comment: '',
        inflow: '',
        outflow: '',
      },
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
    },
    performCreate () {
      const APITransaction = {
        'timestamp': this.newTransaction.date,
        'dossier': {'project': this.account.project},
      }
      if (this.newTransaction.inflow && this.newTransaction.outflow) {
        return
      }
      if (!this.newTransaction.inflow && !this.newTransaction.outflow) {
        return
      }
      if (this.newTransaction.inflow) {
        APITransaction['destination'] = this.$route.params.id
        APITransaction['amount'] = this.newTransaction.inflow
        APITransaction['transactions'] = [{
          'source': this.newTransaction.payee,
          'destination': this.newTransaction.category,
          'amount': this.newTransaction.inflow,
        }]
      } else if (this.newTransaction.outflow) {
        APITransaction['source'] = this.$route.params.id
        APITransaction['amount'] = this.newTransaction.inflow
        APITransaction['transactions'] = [{
          'source': this.newTransaction.category,
          'destination': this.newTransaction.payee,
          'amount': this.newTransaction.inflow,
        }]
      }
      api.realTransactions.create(APITransaction).then((response) => {
        console.log(response)
        this.fetchAccount()
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

  tbody.transaction-list
    :hover
      background-color: $clr-grey-200
    .active, .active :hover
      background-color: $clr-cyan-500

  tbody.transaction-new
    border-bottom: border-separator()

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

  .transaction-input
    > td
      border-bottom-width: 0px
      vertical-align: top

      > .bunt-input
        margin-bottom: 0px
        padding-top: 0px

  .transaction-confirm
    text-align: right

    > td button
      background-color: $clr-cyan-100

</style>
