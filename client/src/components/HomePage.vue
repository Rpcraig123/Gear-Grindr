<template>
  <div>
    <div>
      <div class="nav-bar">
        <b-nav class="logo-text">
          <div class="grid-container">
            <img class="gear-logo" src="../assets/gear5.gif">
            <h2 class="gear-h2">GEAR GRINDR</h2>
            <h3 class="gear-h3">What grinds your gears?</h3>
        
          </div>
        
        </b-nav>
        <form v-on:submit="getSearchResults" @submit.prevent>
          <b-input-group class="mt-1">
            <template #append >
              <!-- <b-input-group-text><strong class="text-danger">!</strong></b-input-group-text> --><b-button type="submit">Search</b-button>
            </template>
            <b-form-input type="search" sm="3" v-model="searchQuery" :value='searchQuery'></b-form-input>
          </b-input-group>
        <!-- <input 
        

        > -->
        <!-- <b-button type="submit" variant="outline-secondary">Search</b-button> -->
        </form>
      </div>
      
    </div>
    <h2>Posts</h2>
    <Modal />
    <section v-if="searched === false">
      <PostCard v-for="post in posts" :post="post" :key="post.id" />
    </section>
    <section v-else>
      <PostCard v-for="post in searchResults" :post="post" :username="username" :key="post.id" />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import PostCard from './PostCard.vue'
import { BASE_URL } from '../globals'
import Modal from './Modal.vue'
// import { b-nav } from 'bootstrap-vue'
export default {
  name: 'Home',
  components: {
    PostCard,
    Modal
  },
  data: () => ({
    posts: [],
    searchQuery: '',
    searchResults: [],
    searched: false
  }),
  mounted: function() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      const res = await axios.get(`${BASE_URL}/post`)
      this.posts = res.data
    },
   
    getSearchResults(){
      let posts = this.posts
      let result = posts.filter(post => post.post.includes(this.searchQuery))
      console.log(result)
      this.searchResults = result
      this.searched = true
    }
  }
}
</script>