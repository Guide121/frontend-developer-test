<template>
  <div id="pricing" class="main-container pricing-container">
    <h1>Choose Your Plan</h1>
    <p>
      Let's choose the package that is best for you and explore it happily and
      cheerfully.
    </p>

    <div class="pricing-plans">
      <PlanCard />

      <PlanCard standard />

      <PlanCard premium />
    </div>
  </div>
</template>

<script></script>

<style scoped>
.pricing-container {
  text-align: center;
  margin-bottom: 100px;
}

h1 {
  color: #0b132a;
  font-weight: 500;
  margin-bottom: 10px;
}

p {
  margin: 0 auto;
  width: 50%;
  color: #4f5665;
}

.pricing-plans {
  margin-top: 50px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
</style>
