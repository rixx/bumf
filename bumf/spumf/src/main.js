import Vue from 'vue'
import Buntpapier from 'buntpapier'

import Main from './main.vue'
import './styles/style.styl'

Vue.use(Buntpapier)
new Vue(Main).$mount('#v-app')
