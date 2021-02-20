<template>
  <div class="main-container network-container">
    <h1 class="title">Huge Global Network of Fast VPN</h1>
    <p class="text">
      See <b>LaslesVPN</b> everywhere to make it easier for you when you move
      locations.
    </p>

    <img src="@/assets/network.png" />
    <img src="@/assets/sponsored.png" />
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.network-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.title {
  margin: 0 auto;
  font-weight: 500;
  font-size: 2.2rem;
  color: #0b132a;
  width: 34%;
  text-align: center;
}

.text {
  color: #4f5665;
  margin: 10px auto;
  text-align: center;
  width: 50%;
  font-weight: 400;
}

img {
  margin: 60px 0;
}
</style>
