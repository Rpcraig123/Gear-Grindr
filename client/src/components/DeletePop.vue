<template>
  <div>
    <div class="mb-2">
    <div class="mb-1">
     <b-button @click="showMsgBoxTwo">msgBoxConfirm with options</b-button>
     Return value: {{ String(boxTwo) }}
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        boxTwo: ''
      }
    },
    methods: {
      showMsgBoxTwo() {
        this.boxTwo = ''
        this.$bvModal.msgBoxConfirm('Please confirm that you want to delete everything.', {
          title: 'Please Confirm Delete',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'danger',
          okTitle: 'Delete',
          cancelTitle: 'Cancel',
          footerClass: 'p-2',
          hideHeaderClose: false,
          centered: true
        })
          .then(value => {
            this.boxTwo = value
          })
          .catch(err => {
            // An error occurred
          })
      }
    }
  }
</script>