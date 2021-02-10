<template>
  <div class="main-container">
    <h1 v-if="!isLoading" class="title">Quadrinhos da Marvel</h1>
    <div v-if="isLoading">
      <md-progress-spinner
        :md-diameter="100"
        :md-stroke="10"
        md-mode="indeterminate"
        class="md-accent"
      ></md-progress-spinner>
    </div>
    <div v-else class="comic-list-container">
      <div v-for="comic in info" :key="comic.id">
        <ComicCard
          :id="comic.id"
          :title="comic.title"
          :image="comic.thumbnail.path + '.' + comic.thumbnail.extension"
          :price="comic.prices[0].price"
        />
      </div>
    </div>
    <div v-if="!isLoading">
      <div class="loadMore" v-if="!loadingMore" v-on:click="getComics">
        Carregar mais
      </div>
      <md-progress-spinner
        v-else
        :md-diameter="50"
        :md-stroke="3"
        md-mode="indeterminate"
        class="md-accent"
      ></md-progress-spinner>
      <div class="info">Foram carregados {{ totalComics }} quadrinhos</div>
    </div>
  </div>
</template>

<script>
import CryptoJs from "crypto-js";

import api from "@/services/marvel";

export default {
  data() {
    return {
      info: this.$store.state.comics,
      totalComics: this.$store.state.comics.length,
      isLoading: true,
      loadingMore: false
    };
  },
  mounted() {
    if (this.info.length > 0) {
      this.isLoading = false;
    } else {
      this.getComics();
    }
  },
  watch: {
    info() {
      if (this.info.length < 200) {
        this.getComics();
      }
    }
  },
  methods: {
    getComics() {
      this.loadingMore = true;

      const timestamp = new Date().getDate();
      const privateKey = process.env.PRIVATE_KEY;
      const publicKey = process.env.PUBLIC_KEY;

      const hash = CryptoJs.MD5(`${timestamp}${privateKey}${publicKey}`);
      const length = this.info.length;

      api
        .get(
          `/comics?offset=${length}&ts=${timestamp}&apikey=${publicKey}&hash=${hash}`
        )
        .then(response => {
          this.$store.commit("getComics", response.data.data.results);

          this.loadingMore = false;
          this.isLoading = false;
          this.totalComics = this.info.length;
        });
    }
  }
};
</script>

<style scoped>
.comic-list-container {
  width: 100%;
  padding: 50px;
  display: grid;
  row-gap: 30px;
  column-gap: 20px;
  grid-template-columns: repeat(4, 1fr);
}

.title {
  text-align: center;
}

.loadMore {
  font-size: 1.4rem;
  cursor: pointer;
  color: cadetblue;
  cursor: pointer;
}

.loadMore:hover {
  text-decoration: underline;
}

.info {
  font-size: 1.2rem;
  text-align: right;
  margin: 20px;
}
</style>
