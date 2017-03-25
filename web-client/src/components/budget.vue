<template>
  <tr>
    <td>
      <div
        :class="{bold: hasChildren}"
        @click="toggle">
        <span v-if="hasChildren">[{{open ? '-' : '+'}}]</span>
      </div>
      {{ model.name }}
    </td>
    <td class="budget-in"></td>
    <td class="budget-out"></td>
    <td class="budget-total">{{ model.total }} €</td>
      <budget-template
        id="budget-template"
        v-for="model in model.child_accounts"
        :model="model">
      </budget-template>
  </tr>
</template>
<script>
export default {
  template: '#budget-template',
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
</script>
