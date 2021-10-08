<template>
  <div>
  <b-button id="show-btn" @click="$bvModal.show('bv-modal-example')">Delete Post</b-button>

  <b-modal id="bv-modal-example" hide-footer>
    <template #modal-title>
     Delete?
    </template>
    <div class="d-block text-center">
      <h3>Are you sure you want to delete this post?</h3>
    </div>
    <b-button class="mt-3" block @click="deletePost(postId)">Delete</b-button>
    </b-modal>
</div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
  export default {
    name: "DeletePop",
    props: ['postId'],
   methods: {
      deletePost(postId) {
      axios.delete(`${BASE_URL}/post/${postId}`)
      this.$bvModal.hide('bv-modal-example')
    }
    }
  }
</script>