<script>
const BudgetTemplate = {
  name: 'budget-template',
  template: '#budget-template',
  render: function (createElement) {
    if (!this.model.child_accounts)
          return ''

    var flatten = function(arr) {
        var result = [];
        for (var i = 0; i < arr.length; i++) {
            if (Array.isArray(arr[i])) {
                result = result.concat(flatten(arr[i]));
            } else {
                result.push(arr[i]);
            }
        }
        return result;
    }

    var getChildren = function(element) {
        if (element.child_accounts && element.child_accounts.length)
            var children = element.child_accounts.map(getChildren)
            if (children) {
                children.every(function (child, index, array) {
                    child.parentObj = element
                })
                return [element].concat(children)
            }
        return element
    }

    var allBudgets = flatten(getChildren(this.model.child_accounts))
    var rows = allBudgets.map(function (element) {
      return createElement(
        'tr',
        [
          createElement('td', {attrs: {class: 'budget-name'}}, element.name),
          createElement('td', {attrs: {class: 'budget-in'}}, ''),
          createElement('td', {attrs: {class: 'budget-out'}}, ''),
          createElement('td', {attrs: {class: 'budget-total'}}, element.total + ' €'),
        ]
      ) 
    })
    return createElement(
      'tbody',
      rows
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
