import auth from 'lib/auth'

const api = {
  login (username, password) {
    return window.fetch('http://127.0.0.1:8000/token-auth/', {
      method: 'POST',
      body: JSON.stringify({username, password}),
      headers: {'Content-Type': 'application/json'}
    })
    .then((response) => {
      return response.json()
    })
    .then((response) => {
      auth.authenticate(response.token)
      return Promise.resolve()
    })
  },

  register (username, password, firstname, email) {
    return window.fetch('http://127.0.0.1:8000/v1/register/', {
      method: 'POST',
      body: JSON.stringify({username, password, first_name: firstname, email}),
      headers: {'Content-Type': 'application/json'}
    })
    .then((response) => {
      return this.login(username, password)
    })
  },

  realAccounts: {
    list () {
      return window.fetch('http://127.0.0.1:8000/v1/real-accounts/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Token ' + auth.authToken,
        }
      })
      .then((response) => {
        return response.json()
      })
    },
    get (id) {
      return window.fetch(`http://127.0.0.1:8000/v1/real-accounts/${id}/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Token ' + auth.authToken,
        }
      })
      .then((response) => {
        return response.json()
      })
    },
  },
  realTransactions: {
    list (accountId) {
      let url = 'http://127.0.0.1:8000/v1/real-transactions/'
      if (accountId) {
        url += `?account_id=${accountId}`
      }
      return window.fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Token ' + auth.authToken,
        }
      })
      .then((response) => {
        return response.json()
      })
    },
  },
}

export default api
