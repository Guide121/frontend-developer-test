<template>
  <div class="card">
    <p class="title">{{ title }}</p>
    <img class="image" :src="image" />
    <p class="price" v-if="price == 0">Gratuito</p>
    <p class="price" v-else>{{ formatedPrice }}</p>

    <button class="button" v-on:click="addToCart">Adicionar ao carrinho</button>
    <n-link :to="{ name: 'comic', params: { id: id } }">Ver mais</n-link>
  </div>
</template>

<script>
export default {
  props: ["title", "image", "id", "price"],
  methods: {
    addToCart() {
      const title = this.title;
      const image = this.image;
      const id = this.id;
      const price = this.price;

      const comic = {
        title,
        image,
        id,
        price
      };

      this.$store.commit("addToCart", comic);
    }
  },
  computed: {
    formatedPrice() {
      return Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
      }).format(this.price);
    }
  }
};
</script>

<style scoped>
.card {
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.7);
  border-radius: 8px;
  margin: 5px;
  padding: 10px;
  height: 340px;

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

.price {
  font-weight: 500;
}

.button {
  padding: 10px;
  border-radius: 5px;
  background: lightgreen;
  border: 0;
  cursor: pointer;
  transition: 0.3s;
  background: #3fa159;
  color: #fff;
  width: 200px;
}

.button:hover {
  background: #2e7741;
}
</style>
