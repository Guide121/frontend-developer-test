<template>
  <div class="container">
    <Header />
    <ComicList />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";

Vue.use(VueMaterial);

export default {
  computed: {
    counter() {
      return this.$store.state.counter;
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Marvel:wght@400;700&display=swap");

.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
