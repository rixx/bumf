<template>
  <bunt-button id="the-button" @click.native="login">
    Knopf.
  </bunt-button>
</template>

<script>
import api from 'lib/api'

export default {
  data () {
    return {
      name: 'Blablubb'
    }
  },
  methods: {
    login () {
      api.login('admin', 'admin') 
    },
  },
}
</script>

<style lang="stylus">
@import '~_settings'

#the-button
  button-style(color: $clr-danger)
</style>
