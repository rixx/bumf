import auth from 'lib/auth'

const api = {
  http (verb, url, headers, body) {
    var fullHeaders = JSON.parse(JSON.stringify(headers)) || {}
    fullHeaders['Content-Type'] = fullHeaders['Content-Type'] || 'application/json'

    if (!fullHeaders['Authorization'] && auth.authToken) {
      fullHeaders['Authorization'] = 'Token ' + auth.authToken
    }

    let options = {
      method: verb || 'GET',
      headers: fullHeaders,
      body: body && JSON.stringify(body)
    }
    return window.fetch(url, options).then((response) => {
      if (response.status === 204) {
        return Promise.resolve()
      }
      return response.json().then((json) => {
        if (!response.ok) {
          return Promise.reject({response, json})
        }
        return Promise.resolve(json)
      })
    }).catch((error) => {
      return Promise.reject(error)
    })
  },

  login (username, password) {
    return api.http(
      'POST',
      'http://127.0.0.1:8000/token-auth/',
      null,
      {username, password}
    ).then((response) => {
      auth.authenticate(response.token, username)
      return Promise.resolve()
    })
  },

  logout () {
    auth.logout()
  },

  register (username, password, firstname, email) {
    return api.http(
      'POST',
      'http://127.0.0.1:8000/v1/register',
      null,
      {username, password, first_name: firstname, email}
    ).then((response) => {
      return this.login(username, password)
    })
  },

  realAccounts: {
    list () {
      return api.http('GET', 'http://127.0.0.1:8000/v1/real-accounts/', null, null)
    },
    get (id) {
      return api.http('GET', `http://127.0.0.1:8000/v1/real-accounts/${id}/`, null, null)
    },
  },
  budgetAccounts: {
    list () {
      return api.http('GET', 'http://127.0.0.1:8000/v1/budget-accounts/', null, null)
    },
    get (id) {
      return api.http('GET', `http://127.0.0.1:8000/v1/budget-accounts/${id}/`, null, null)
    },
  },
  realTransactions: {
    list (accountId) {
      let url = 'http://127.0.0.1:8000/v1/real-transactions/'
      if (accountId) {
        url += `?account_id=${accountId}`
      }
      return api.http('GET', url, null, null)
    },
    create (transaction) {
      let url = 'http://127.0.0.1:8000/v1/real-transactions/'
      return api.http('POST', url, null, transaction)
    }
  },
}

export default api
