<template>
  <div id="app">
    <h3>A full stack application made with Vue.JS and Flask (Python)</h3>
    <RentPredictor/>
    <div id="portfolio-link"><h4> To view more of my projects<a href="https://sites.google.com/view/juanfernandezportfolio/project-page" target="_blank" rel="noopener noreferrer"> click here</a> to be directed to my Portfolio Website.</h4></div>
  </div>
</template>

<script>
import RentPredictor from './components/RentPredictor.vue'

  export default {
    name: 'App',
    components: {
      RentPredictor
    },
    data() {   
      return {
        started: false
      }
    }
  }

</script>

<style>
* {
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  padding: 20px;
}

#app {
  max-width: 600px;
  margin: 0 auto;
}

h3 {
  text-align: center;
  margin-bottom: 5px;
}
a {
  text-decoration: none;
  color: white;
  }
a:hover {
color: #D8CFF8;
}
</style>
