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
        />
      </div>
    </div>
  </div>
</template>

<script>
import CryptoJs from "crypto-js";
import { MdProgressSpinner } from "vue-material";

import api from "@/services/marvel";

export default {
  data() {
    return {
      info: [],
      isLoading: true
    };
  },
  mounted() {
    const timestamp = new Date().getDate();
    const privateKey = process.env.PRIVATE_KEY;
    const publicKey = process.env.PUBLIC_KEY;

    const hash = CryptoJs.MD5(`${timestamp}${privateKey}${publicKey}`);

    api
      .get(`/comics?ts=${timestamp}&apikey=${publicKey}&hash=${hash}`)
      .then(response => {
        this.isLoading = false;
        this.info = response.data.data.results;
      });
  },
  methods: {
    getRandomNumber() {
      return Math.floor(Math.random() * this.info.length);
    },
    addToFavorites(comidId) {
      const favoriteComicsList =
        JSON.parse(localStorage.getItem("favoriteComics")) || [];

      favoriteComicsList.push(comidId);

      localStorage.setItem(
        "favoriteComics",
        JSON.stringify(favoriteComicsList)
      );
    }
  },
  computed: {
    infoRaro() {
      return Array.from({ length: 10 }, () => this.getRandomNumber());
    }
  }
};
</script>

<style scope>
.comic-list-container {
  width: 100%;
  padding: 50px;
  display: grid;
  row-gap: 30px;
  column-gap: 20px;
  grid-template-columns: repeat(4, 1fr);
}
</style>
