import Account from './views/account'
import App from './app'
import Budget from './views/budget'
import Login from './views/login'

const routes = [{
  path: '/',
  component: App,
  meta: {requiresAuth: true},
  children: [
    {
      path: 'budget',
      name: 'budget',
      component: Budget,
    },
    {
      path: 'account/:id',
      name: 'account',
      component: Account,
    }
  ],
}, {
  path: '/login',
  component: Login
}]

export default routes
