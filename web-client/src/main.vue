<template>
    <router-view></router-view>
</template>

<script>
export default {
  data () {
    return {
      name: 'Blablubb'
    }
  }
}
</script>

<style lang="stylus">
@import '~_settings'

#main #the-button
  button-style(color: $clr-danger)
</style>
