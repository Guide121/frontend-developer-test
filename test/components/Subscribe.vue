<template>
  <div class="main-container subscribe-container">
    <div class="info">
      <h1 class="title">Subscribe Now for Get Special Features!</h1>
      <p class="text">Let's subscribe with us and find the fun.</p>
    </div>

    <Button title="Subscribe now" primary />
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.subscribe-container {
  background: #fff;
  width: 90%;
  padding: 20px;
  box-shadow: 0px 5px 15px rgba(13, 16, 37, 0.1);
  margin: 20px auto;
  border-radius: 10px;

  display: flex;
  align-items: center;
  justify-content: space-around;

  position: relative;
  z-index: 2;
}

.info {
  width: 50%;
}

.title {
  color: #0b132a;
  font-weight: 500;
  width: 57%;
}

.text {
  margin: 10px 0;
  color: #4f5665;
}
</style>
