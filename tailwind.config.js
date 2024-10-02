/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
],
  theme: {
    extend: {
      fontFamily: {
        font: ['eqolia' ,'sans-serif'],
      },
  },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}