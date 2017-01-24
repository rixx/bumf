import App from './app'
import Login from './login'

const routes = [{
    path: '/',
    component: App,
    meta: {requiresAuth: true},
    children: [],
  }, {
    path: '/login',
    component: Login
}]

export default routes
