<template>
  <div class="main-container info">
    <div>
      <img src="@/assets/user.png" />
      <div class="text">
        <p class="number">90+</p>
        <p class="card-info">Users</p>
      </div>
    </div>
    <div>
      <img src="@/assets/location.png" />
      <div class="text">
        <p class="number">30+</p>
        <p class="card-info">Locations</p>
      </div>
    </div>
    <div>
      <img src="@/assets/server.png" />
      <div class="text">
        <p class="number">50+</p>
        <p class="card-info">Servers</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.info {
  margin: 100px auto 50px;
  column-count: 3;
  column-rule: 2px solid #eeeff2;
  background: #fff;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0px 5px 15px rgba(13, 16, 37, 0.1);
}

.info div {
  display: flex;
  height: 100px;
  justify-content: center;
  align-items: center;
}

.info div .text {
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.number {
  color: #0b132a;
  font-weight: 700;
}

.card-info {
  color: #4f5665;
}
</style>
