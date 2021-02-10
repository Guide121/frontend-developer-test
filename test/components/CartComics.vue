<template>
  <div class="cart-comic">
    <img class="comic-img" :src="image" />

    <div class="comic-info">
      <p>{{ formatedTitle }}</p>
      <p>
        {{ formatedPrice }}
      </p>
      <button class="button" v-on:click="removeFromCart">
        Remover do carrinho
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title", "id", "price", "image"],
  computed: {
    formatedPrice() {
      return Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
      }).format(this.price);
    },
    formatedTitle() {
      if (this.title.length > 20) {
        return this.title.slice(0, 20) + "...";
      }

      return this.title;
    }
  },
  methods: {
    removeFromCart() {
      this.$store.commit("removeFromCart", this.id);
    }
  }
};
</script>

<style scoped>
.cart-comic {
  display: flex;
  margin: 5px 0;
}

.comic-img {
  width: 80px;
  height: 120px;
}

.comic-info {
  height: 120px;
  margin-left: 20px;
  font-size: 12px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: space-between;
  font-weight: 500;
}

.button {
  padding: 4px;
  background: #ee403c;
  border: 0;
  cursor: pointer;
  border-radius: 5px;
  color: #fff;
}
</style>
