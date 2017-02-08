const auth = {
  authToken: localStorage.getItem('authToken'),
  authenticated: localStorage.getItem('authToken') !== null,
  authenticate (token) {
    localStorage.setItem('authToken', token)
    auth.authToken = token
    auth.authenticated = true
  }
}

export default auth
