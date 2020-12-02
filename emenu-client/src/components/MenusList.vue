<template>
  <v-app>
  <v-data-table
    :headers="headers"
    :items="menus"
    :hide-actions="true"
    class="elevation-1"
  >
    <template v-slot:items="menus">
      <td>{{ menus.item.id }}</td>
      <td>{{ menus.item.name }}</td>
      <td>{{ menus.item.description }}</td>
      <td>{{ menus.item.total_courses }}</td>
      <td><router-link :to="{
      name: 'MenuDetails',
      params: { id: menus.item.id }
      }">Show</router-link></td>
    </template>
  </v-data-table>
  <div class="text-center">
    <v-pagination
      v-model="page"
      :length="allPages"
      prev-icon="mdi-menu-left"
      next-icon="mdi-menu-right"
    ></v-pagination>
  </div>
</v-app>
</template>
<script>

import api from '../api'
export default {
  data () {
    return {
      allPages: 0,
      page: 1,
      headers: [
        { text: 'No.', value: 'id'},
        {
          text: 'Name',
          align: 'left',
          value: 'name'
        },
      {
        text: 'Description',
        value: 'description',
        sortable: false
      },
        {
          text: 'Courses',
          value: 'total_courses'
        },
        {
          text: 'Show',
          value:'id',
          sortable:false
        }
        ]
      }
  },
  methods: {
    getCount(){
      api.get('menus/count/')
          .then((response) => {
        const allMenus = response.data.count;
        if (allMenus < 10){
          this.allPages = 1;
        }else {
          this.allPages = (allMenus / 10) + 1;
        }
      })
    }
  },
  asyncComputed: {
    menus: {
      async get() {
        const response = await api.get('menus?not_empty=True&page=' + this.page);
        console.log(response.data.results)
        return response.data.results;
      },
      default: []
    }
  },
  created: function() {
    this.getCount();
  }
}
</script>

<style >
</style>