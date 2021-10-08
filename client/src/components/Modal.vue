<template>
  <div>
    <div>
      <b-button v-b-modal.modal-prevent-closing class="post-button">Create A Post</b-button>

      <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Submit Your Post"
      hide-footer
      >
      <b-form ref="form" @submit="newPost">
        <b-form-group
          label="username"
          label-for="username-input"
          invalid-feedback="Username is required"
          
        >
          <b-form-input
            id="username-input" 
            
            v-model="username"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="post" label-for="post-input" invalid-feedback="Content is required" >
          <b-form-input id="post-input" v-model="post" ></b-form-input>
        </b-form-group>

      <b-button class="mt-3" block @click="newPost">Submit</b-button>
      </b-form>
    </b-modal>
    </div>
  </div>
</template>

<script>
import {BModal, BButton, BFormInput, BForm, BFormGroup} from 'bootstrap-vue'
import axios from 'axios'
import {BASE_URL} from '../globals'
export default {
  name: 'Modal',
  data: () =>({
    username: '',
    post: ''
  }),
  components: {
    BModal,
    BButton,
    BFormInput,
    BForm,
    BFormGroup
  },
  methods: {
      async newPost(){
        const res = await axios.post(`${BASE_URL}/post`, 
        {
          username: this.username,
          post: this.post
        })
        this.username = ''
        this.post = ''
        location.reload()
        return res
      }
  }
}
</script>

<style>

</style>