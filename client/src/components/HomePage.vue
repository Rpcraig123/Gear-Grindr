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
// import axios from 'axios'
import PostCard from './PostCard.vue'
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
      // const res = await axios.get(``)
      // this.posts = res.data.results
      // console.log('getPosts successfully ran')
    }
  }
}
</script>