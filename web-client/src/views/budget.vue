<template>
  <div class="budget" v-if="budgets">
    <div id="budget-header"></div>
    <table id="budget-table">
      <thead>
        <th></th>
        <th>Budgeted this month</th>
        <th>Spent this month</th>
        <th>Total</th>
      </thead>
      <tbody>
        <tr v-for="budget in budgets">
          <td>{{ budget.name }}</td>
          <td></td>
          <td></td>
          <td>{{ budget.total }}</td>
        </tr>
    </table>
  </div>
</template>

<script>
import api from 'lib/api'
export default {
  components: {},
  data () {
    return {
      budgets: []
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
        this.budgets = result
      })
    }
  }
}
</script>

<style lang="stylus">
.budget
  width: 100%

#budget-header
  width: 100%
  background-color: $clr-cyan-700
  padding: 8px

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

  thead th
    background-color: $clr-cyan-100
    font-weight: normal
    padding: 16px
    height: 0px
</style>
