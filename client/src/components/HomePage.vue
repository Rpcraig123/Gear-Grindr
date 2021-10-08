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
      </div>
    </div>
    <h2>Posts</h2>
    <Modal />
    <section>
      <PostCard v-for="post in posts" :post="post" :username="username" :key="post.id" />
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
  }),
  mounted: function() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      const res = await axios.get(`${BASE_URL}/post`)
      this.posts = res.data
      console.log("res", res.data)
    }
  }
}
</script>