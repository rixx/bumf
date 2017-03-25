<template>
  <div class="budget" v-if="budgets">
    <div id="budget-header"></div>
    <div class="budget-body">
      <div class="budget-table">
      <table id="budget-table">
        <thead>
          <th class="budget-name"></th>
          <th class="budget-in">Budgeted this month</th>
          <th class="budget-out">Spent this month</th>
          <th class="budget-total">Total</th>
        </thead>
        <tbody>
          <budget-template id="budget-template" :model="budgets">
          </budget-template>
          <tr v-for="budget in budgets.child_accounts" @click="activeBudget=(budget === activeBudget) ? null : budget" :class="{active: budget === activeBudget}">
            <td class="budget-name">{{ budget.name }}</td>
            <td class="budget-in"></td>
            <td class="budget-out"></td>
            <td class="budget-total">{{ budget.total }} €</td>
          </tr>
      </table>
      </div>
      <div class="budget-detail" v-if="activeBudget">
        <h3 id="active-name">{{ activeBudget.name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import api from 'lib/api'
import BudgetTemplate from 'components/budget'
export default {
  components: {BudgetTemplate},
  data () {
    return {
      activeBudget: null,
      budgets: {},
    }
  },
  computed: {},
  created () {
    this.fetchBudgets()
  },
  mounted () {
    this.$nextTick(() => {
    })
  },
  methods: {
    fetchBudgets () {
      api.budgetAccounts.list().then((result) => {
        this.budgets = {child_accounts: result, name: "root"}
      })
    }
  }
}
</script>

<style lang="stylus">
.budget
  width: 100%

.budget-body
  display: flex
  flex-direction: row
  flex-wrap: nowrap

.budget-detail
  background-color: $clr-cyan-700
  flex-grow: 0
  width: 320px

#budget-header
  width: 100%
  background-color: $clr-cyan-700
  padding: 8px

.budget-table
  flex-shrink: 1
  flex-grow: 1

#budget-table
  margin: 0
  table()

  tbody
    :hover
      background-color: $clr-grey-200
    .active, .active :hover
      background-color: $clr-cyan-500

  tbody td
    border-bottom: border-separator()
    height: 0px
    padding: 8px

  .budget-in, .budget-out
    text-align: right
    width: 120px

  .budget-total
    text-align: right
    width: 80px

  thead th
    background-color: $clr-cyan-100
    font-weight: normal
    padding: 16px
    height: 0px
</style>
