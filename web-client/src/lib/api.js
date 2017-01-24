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
  }
}

export default api
