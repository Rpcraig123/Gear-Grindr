<template>
  <div>
    <button>Create a Post</button>
    <h2>Posts</h2>
    <section>
      <PostCard v-for="post in posts" :post="post" :username="username" :key="post.id" />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import PostCard from './PostCard.vue'
import { BASE_URL } from '../globals'
export default {
  name: 'Home',
  components: {
    PostCard
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