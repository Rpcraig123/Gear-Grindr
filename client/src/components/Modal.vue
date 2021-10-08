<template>
  <div>
    <div>
      <b-button v-b-modal.modal-prevent-closing>Create A Post</b-button>

      <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Submit Your Name"
    >
      <form ref="form" @submit.stop.prevent="onSubmit">
        <b-form-group
          label="username"
          label-for="username-input"
          invalid-feedback="Username is required"
          :state="username"
        >
          <b-form-input
            id="username-input"
            v-model="username"
            :state="username"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="post" label-for="post-input" invalid-feedback="Content is required" :state="post">
          <b-form-input id="conent-input" v-model="post" :state="post"></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
    </div>
  </div>
</template>

<script>
import {BModal, BButton, BFormInput, BFormGroup} from 'bootstrap-vue'
import axios from 'axios'
import {BASE_URL} from '../globals'
export default {
  name: 'Modal',
  data: () =>({
    username: null,
    post: null
  }),
  components: {
    BModal,
    BButton,
    BFormInput,
    BFormGroup
  },
  methods: {
      async newPost(){
        await axios.post(`${BASE_URL}/post`, 
        {
          username: this.username,
          post: this.post
        })
      },
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
        this.newPost()
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.username = ''
        this.form.post = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
  }
}
</script>

<style>

</style>