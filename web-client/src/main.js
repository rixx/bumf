import Buntpapier from 'buntpapier'
import VueRouter from 'vue-router'
import Vue from 'vue'

import auth from 'lib/auth'
import Main from './main.vue'
import routes from './routes'

import './styles/style.styl'

Vue.use(Buntpapier)
Vue.use(VueRouter)

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !auth.authenticated) {
      next('/login')
  } else {
      next()
  }
})

Main.router = router
new Vue(Main).$mount('#v-app')
