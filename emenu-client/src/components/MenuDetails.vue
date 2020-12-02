<template>
  <v-data-table
    :headers="headers"
    :items="courses"
    :hide-actions="true"
    :rows-per-page-items = "-1"
    :class="elevation-1"
  >
    <template v-slot:items="courses">
      <td>{{ courses.item.id }}</td>
      <td>
        <v-img
        :lazy-src="courses.item.image"
        :src="courses.item.image"
        ></v-img>
      </td>
      <td>{{ courses.item.name }}</td>
      <td>{{ courses.item.description }}</td>
      <td>{{ courses.item.preparation_time}}</td>
    </template>
  </v-data-table>
</template>
<script>

import api from '../api'
export default {
  data () {
    return {
      courses: [],
      headers: [
        { text: 'No.', value: 'id'},
        {
          text: 'Image',
          value: 'image',
          sortable: false
        },
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
          text: "Preparation time",
          value: "preparation_time"
        }
        ]
    }
  },
  methods: {
    fetchCourses () {
      api.get('courses?menu='+this.$route.params.id)
          .then((response) => {
            this.courses = response.data.results;
          })
    }
  },
  created: function () {
    this.fetchCourses()
  }
}
</script>

<style scoped>
</style>