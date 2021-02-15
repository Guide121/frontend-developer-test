<template>
  <div class="main-container features-container">
    <img src="@/assets/features.png" />

    <div class="info">
      <h1>We Provide Many Features You Can Use</h1>

      <p>
        You can explore the features that we provide with fun and have their own
        functions each feature.
      </p>

      <ul>
        <li>
          <img src="@/assets/correct.png" />
          <p>Powerfull online protection.</p>
        </li>
        <li>
          <img src="@/assets/correct.png" />
          <p>Internet without borders.</p>
        </li>
        <li>
          <img src="@/assets/correct.png" />
          <p>Supercharged VPN</p>
        </li>
        <li>
          <img src="@/assets/correct.png" />
          <p>No specific time limits.</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.features-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 90vh;
}

.info {
  margin-left: 100px;
  width: 37%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  height: 300px;
}

.info h1 {
  color: #0b132a;
  font-weight: 500;
  width: 80%;
}

.info p {
  color: #4f5665;
}

ul {
  list-style: none;
  width: 100%;
  padding-left: 0;
  height: 150px;
}

ul li {
  display: flex;
  align-items: center;
}

ul li p {
  margin: 10px;
  font-size: 0.9rem;
}
</style>
