<template>
  <div>
    <div>
      <BButton v-b-modal.modal-1>Launch demo modal</BButton>

      <BModal id="modal-1" title="BootstrapVue">
        <p class="my-4">Hello from modal!</p>
      </BModal>
    </div>
  </div>
</template>

<script>
import {BModal, BButton} from 'bootstrap-vue'
export default {
  name: 'Modal',
  components: {
    BModal,
    BButton
  }

}
</script>

<style>

</style>