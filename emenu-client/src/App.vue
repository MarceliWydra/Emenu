<template>
  <v-app id="inspire">
    <v-main>
    <v-container>
        <div id="app">
    <router-view></router-view>
  </div>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
