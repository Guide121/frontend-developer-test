<template>
  <div>
    <md-menu md-direction="bottom-start">
      <md-button md-menu-trigger class="text">Carrinho</md-button>

      <md-menu-content>
        <md-menu-item v-for="(info, key) in list" :key="key">{{
          info
        }}</md-menu-item>
      </md-menu-content>
    </md-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: ["teste", "teste2", "teste3"]
    };
  }
};
</script>

<style scoped>
.text {
  color: #fff;
  font-size: 1.8rem;
}
</style>
