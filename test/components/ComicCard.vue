<template>
  <div class="card">
    <p class="title">{{ title }}</p>
    <img class="image" :src="image" />
    <n-link :to="{ name: 'comic', params: { id: id } }">Ver mais</n-link>
  </div>
</template>

<script>
export default {
  props: ["title", "image", "id"],
  methods: {
    increment(e) {
      this.$store.commit("increment");
    },
    decrement(e) {
      this.$store.commit("decrement");
    }
  }
};
</script>

<style scope>
.card {
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.7);
  border-radius: 8px;
  margin: 5px;
  padding: 10px;
  height: 300px;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.title {
  font-weight: 700;
}

.image {
  width: 100px;
}
</style>
