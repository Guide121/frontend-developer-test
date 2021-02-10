<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />

    <md-menu md-direction="bottom-start" md-size="big" md-align-trigger>
      <md-badge class="md-primary" :md-content="list.length">
        <md-button md-menu-trigger class="md-icon-button">
          <md-icon id="icon">shopping_cart</md-icon>
        </md-button>
      </md-badge>

      <md-menu-content>
        <md-menu-item class="items" v-for="(comic, key) in list" :key="key">
          <CartComics
            :title="comic.title"
            :image="comic.image"
            :id="comic.id"
            :price="comic.price"
          />
        </md-menu-item>
        <div class="total">
          <div v-if="list.length === 0">Não há itens no carrinho</div>
          <div v-else>Total: {{ totalPrice }}</div>
        </div>
      </md-menu-content>
    </md-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: this.$store.state.cart
    };
  },
  computed: {
    totalPrice() {
      const totalPrice = this.$store.state.cart.reduce(
        (acc, { price }) => (acc += price),
        0
      );

      return Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
      }).format(totalPrice);
    }
  }
};
</script>

<style scoped>
.text {
  color: #fff;
  font-size: 1.8rem;
}

#icon {
  color: #fff;
}

.total {
  margin-left: 10px;
  font-weight: 600;
}
</style>
