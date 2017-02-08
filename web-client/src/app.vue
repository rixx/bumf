<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './navbar'
export default {
  components: {Navbar},
  data () {
    return {
    }
  },
  computed: {},
  created () {},
  mounted () {
    this.$nextTick(() => {
    })
  },
  methods: {}
}
</script>

<style lang="stylus">
</style>
