<script>
const BudgetTemplate = {
  name: 'budget-template',
  template: '#budget-template',
  render: function (createElement) {
    var getChildren = function(element) {
       return element.child_accounts ? element + element.child_accounts.map(getChildren) : element 
    }
    var allBudgets = getChildren(this.props.model.child_accounts)
    rows = allBudgets.map(function (element) {
      createElement(
        'tr',
        [
          createElement('th', 'something!'),
          createElement('th'),
          createElement('th'),
          createElement('th'),
        ]
      ) 
    })
    return createElement(
      'tbody',
      rows,
    )
  },
  props: {
    model: Object
  },
  data: function () {
    return {
      open: true
    }
  },
  computed: {
    hasChildren: function () {
      return this.model.child_accounts &&
        this.model.child_accounts.length
    }
  },
  methods: {
    toggle: function () {
      if (this.hasChildren) {
        this.open = !this.open
      }
    },
  }
}
export default BudgetTemplate
</script>
