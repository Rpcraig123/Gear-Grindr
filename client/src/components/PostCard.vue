<template>
  <div>
    <b-card bg-variant="light" :header="post.username" class="text-center">
        <b-card-text>{{post.post}}</b-card-text>
        <b-button @click="deletePost(post.id)" variant="primary">Delete Post</b-button>
    </b-card>
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
      this.$forceUpdate()
    }
  }
}
</script>