import Vue from 'vue'
import Router from 'vue-router'
import MenuDetails from "./components/MenuDetails";
import MenusList from './components/MenusList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MenuList',
      component: MenusList
    },
    {
      path: '/menu/:id(\\d+)',
      name: 'MenuDetails',
      component: MenuDetails,
      props: true
    }
  ]
})