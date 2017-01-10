<template>
<div id="main">
  <h1>Hello world!!</h1>

  {{ name }}

  <bunt-button id="the-button" @click.native="name=123">A button</bunt-button>
</div>
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
