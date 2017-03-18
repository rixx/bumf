<template>
  <div class="budget" v-if="budgets">
    {{ budgets }}
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
