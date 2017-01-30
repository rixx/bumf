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
  }
}

export default api
