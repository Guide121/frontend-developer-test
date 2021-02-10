<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />

    <Header />
    <div class="container">
      <n-link to="/">
        < Voltar
      </n-link>

      <div v-if="isLoading">
        <md-progress-spinner
          :md-diameter="100"
          :md-stroke="10"
          md-mode="indeterminate"
          class="md-accent"
        ></md-progress-spinner>
      </div>

      <div class="info-comic" v-else>
        <img
          :src="infoComic.thumbnail.path + '.' + infoComic.thumbnail.extension"
        />
        <div class="info">
          <p class="title">{{ infoComic.title }}</p>
          <p v-if="infoComic.description === null">Não há descrição</p>
          <p v-else>{{ infoComic.description }}</p>
          <p id="price">Preço: {{ formatedPrice }}</p>

          <button class="button" v-on:click="addToCart">Comprar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/marvel";
import CryptoJs from "crypto-js";

export default {
  data() {
    return {
      infoComic: {},
      isLoading: true
    };
  },
  mounted() {
    const id = this.$route.params.id;

    const timestamp = new Date().getDate();
    const privateKey = process.env.PRIVATE_KEY;
    const publicKey = process.env.PUBLIC_KEY;

    const hash = CryptoJs.MD5(`${timestamp}${privateKey}${publicKey}`);

    api
      .get(`/comics/${id}?ts=${timestamp}&apikey=${publicKey}&hash=${hash}`)
      .then(res => {
        this.isLoading = false;
        console.log(res.data.data.results[0]);
        return (this.infoComic = res.data.data.results[0]);
      });
  },
  computed: {
    formatedPrice() {
      return Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL"
      }).format(this.infoComic.prices[0].price);
    }
  },
  methods: {
    addToCart() {
      const title = this.infoComic.title;
      const image =
        this.infoComic.thumbnail.path +
        "." +
        this.infoComic.thumbnail.extension;
      const id = this.infoComic.id;
      const price = this.infoComic.prices[0].price;

      const comic = {
        title,
        image,
        id,
        price
      };

      this.$store.commit("addToCart", comic);
    }
  }
};
</script>

<style scoped>
.container {
  width: 95%;
  margin: 20px auto 0;
}

.info-comic {
  margin-top: 30px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

img {
  width: 20%;
}

.info {
  font-size: 1rem;
  display: flex;
  height: 300px;
  width: 50%;
  flex-direction: column;
  justify-content: space-between;
}

.title {
  font-weight: 500;
  text-align: center;
  font-size: 1.2rem;
}

#price {
  text-align: left;
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
