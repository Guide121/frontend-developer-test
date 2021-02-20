<template>
  <div id="about" class="main-container about-container">
    <div class="info">
      <h1>Want anything to be easy with <b>LaslesVPN.</b></h1>

      <p>
        Provide a network for all your needs with ease and fun using
        <b>LaslesVPN</b>
        discover interesting features from us.
      </p>

      <Button title="Get Start" primary />
    </div>

    <img src="@/assets/about.png" />
  </div>
</template>

<script>
export default {
  methods: {
    printConsole() {
      console.log('a')
    },
  },
}
</script>

<style scoped>
.about-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70vh;
}

.info {
  width: 50%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
}

h1 {
  color: #0b132a;
  font-weight: 500;
  width: 70%;
  font-size: 2.4rem;
}

h1 b,
p b {
  font-weight: 700;
}

p {
  color: #4f5665;
  width: 90%;
  /* margin: 20px 0; */
}
</style>
