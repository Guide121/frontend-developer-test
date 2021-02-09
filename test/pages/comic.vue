<template>
  <div class="main-container">
    <nuxt-link to="/">Voltar</nuxt-link>
    <Header />
    <div v-if="isLoading">Carregando</div>
    <div v-else>
      {{ infoComic.title }}
      <img
        :src="infoComic.thumbnail.path + '.' + infoComic.thumbnail.extension"
      />
    </div>
  </div>
  <!-- </div> -->
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
  }
};
</script>
