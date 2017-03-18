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
</style>
