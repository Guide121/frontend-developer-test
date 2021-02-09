<template>
  <div>
    <button v-on:click="increment">Incrementar</button>
    <button v-on:click="decrement">Decrementar</button>
  </div>
</template>

<script>
export default {
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
