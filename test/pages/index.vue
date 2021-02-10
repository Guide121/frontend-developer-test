<template>
  <div>
    <Header />
    <div class="container">
      <ComicList />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";

Vue.use(VueMaterial);

export default {};
</script>

<style scoped>
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

<style>
@import url("https://fonts.googleapis.com/css?family=Roboto:400,500,700,400italic%7cmaterial+Icons");
</style>
