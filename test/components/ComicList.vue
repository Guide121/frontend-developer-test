<template>
  <div class="comic-list-container">
    Hello world
  </div>
</template>

<script>
import axios from "axios";
import CryptoJs from "crypto-js";

import api from "@/services/marvel";

export default {
  data() {
    return {
      info: []
    };
  },
  mounted() {
    const timestamp = new Date().getDate();
    const privateKey = process.env.PRIVATE_KEY;
    const publicKey = process.env.PUBLIC_KEY;

    const hash = CryptoJs.MD5(`${timestamp}${privateKey}${publicKey}`);

    api
      .get(
        `$/v1/public/comics?ts=${timestamp}&apikey=${publicKey}&hash=${hash}`
      )
      .then(response => console.log(response));
  }
};
</script>

<style scope>
.comic-list-container {
  width: 100%;
}
</style>
