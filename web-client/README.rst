bumf: web frontend
------------------

Development
===========

```shell
npm install
npm run server
```

The bumf web frontend uses three languages:

- JavaScript

  - ES2015 and Stage 3 features provided by babel
  - Linting with eslint

- Stylus

  - Preprocesses CSS (comparable to SASS or LESS)
  - No linting atm
  - don't use `{} or ;`
  - use `: ` between property and value
  - prefix variables with `$`

- Plain HTML

  - No linting yet

`.vue` files combine ES, HTML template and stylus sheets into one file.

Folder structure
================

::

    ┣━━ build/: webpack configs and build scripts
    ┣━━ src/: code
    ┃   ┣━━ assets/: static files
    ┃   ┣━━ components/: reusable vue components
    ┃   ┣━━ lib/: plain js modules
    ┃   ┣━━ styles/: global styles and stylus modules
    ┃   ┣━━ views/: vue components for specific routes (directory structure follows url structure)
    ┃   ┣━━ routes.js: routes
    ┃   ┣━━ main.js: app entry point
    ┃   ┣━━ main.vue: "body" component, only contains the root router-view
