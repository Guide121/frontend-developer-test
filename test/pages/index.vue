<template>
  <div class="container">
    <Header />
    <ComicList />
  </div>
</template>

<script lang="ts">
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
