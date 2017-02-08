import Vue from 'vue'
import moment from 'moment'

const dateFormat = 'YYYY-MM-DD'
const datetimeFormat = 'YYYY-MM-DD hh:mm'

Vue.filter('date', (date) => {
  return moment(date).format(dateFormat)
})
Vue.filter('datetime', (date) => {
  return moment(date).format(datetimeFormat)
})

Vue.filter('fromnow', (date) => {
  return moment(date).fromNow()
})
Vue.filter('truncate', (str, length) => {
  return (str.length > length ? str.slice(0, length - 1) + '…' : str)
})
