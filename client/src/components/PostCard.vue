<template>
  <div>
    <h2>{post.username}</h2>
    <p>{post.post}</p>
    <button @click="deletePost()"></button>
  </div>
</template>

<script>
export default {
  name: 'PostCard',
  props: ['post'],
  methods: {
    deletePost(postId) {
      console.log("delete ran")
      // await axios.delete(``)
    }
  }
}
</script>