<template>
  <div v-if="loading" class="loading-page">
    <md-progress-spinner
      :md-diameter="100"
      :md-stroke="10"
      md-mode="indeterminate"
    ></md-progress-spinner>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: false
  }),
  methods: {
    start() {
      this.loading = true;
    },
    finish() {
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.loading-page {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding-top: 200px;
  font-size: 30px;
  font-family: sans-serif;
}
</style>
