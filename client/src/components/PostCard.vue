<template>
  <div>
    <h2>{post.username}</h2>
    <p>{post.post}</p>
    <button @click="deletePost(post.id)"></button>
  </div>
</template>

<script>
import { BASE_URL } from '../globals'
import axios from 'axios'
export default {
  name: 'PostCard',
  props: ['post'],
  methods: {
    deletePost(postId) {
      axios.delete(`${BASE_URL}/post/${postId}`)
      console.log("delete ran")
    }
  }
}
</script>