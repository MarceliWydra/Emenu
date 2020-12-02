import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import api from './api'
import AsyncComputed from 'vue-async-computed'
import router from './router'

Vue.config.productionTip = false
Vue.prototype.$http = api

Vue.use(AsyncComputed);


new Vue({
  el: '#app',
  router,
  AsyncComputed,
  render: h => h(App),
  state: {
    page: 1
  }
}).$mount('#app')
