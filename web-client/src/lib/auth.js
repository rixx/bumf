const auth = {
  authenticated: localStorage.getItem('authToken') !== null,
  authenticate (token) {
    localStorage.setItem('authToken', token)
    auth.authenticated = true
  }
}

export default auth
