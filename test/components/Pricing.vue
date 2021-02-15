<template>
  <div class="main-container pricing-container">
    <h1>Choose Your Plan</h1>
    <p>
      Let's choose the package that is best for you and explore it happily and
      cheerfully.
    </p>

    <div class="pricing-plans">
      <div class="plan">
        <img src="@/assets/plan.png" />
        <p>Free Plan</p>

        <ul>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Unlimited Bandwitch</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Encrypted Connection</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">No Traffic Logs</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Works on All Devices</span>
          </li>
        </ul>

        <Button title="Select" />
      </div>

      <div class="plan">
        <img src="@/assets/plan.png" />
        <p>Standard Plan</p>

        <ul>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Unlimited Bandwitch</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Encrypted Connection</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">No Traffic Logs</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Works on All Devices</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Connect Anyware</span>
          </li>
        </ul>

        <Button title="Select" />
      </div>

      <div class="plan selected">
        <img src="@/assets/plan.png" />
        <p>Premium Plan</p>

        <ul>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Unlimited Bandwitch</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Encrypted Connection</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">No Traffic Logs</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Works on All Devices</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Connect Anyware</span>
          </li>
          <li>
            <img src="@/assets/correct2.png" />
            <span class="plan-info">Get New Features</span>
          </li>
        </ul>

        <Button title="Select" primary bordered />
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

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

.plan {
  width: 25%;
  height: 90vh;
  border-radius: 10px;
  border: 2px solid #dddddd;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
}

.plan p {
  color: #0b132a;
  font-weight: 500;
  margin-top: 20px;
}

ul {
  list-style: none;
  padding-left: 0;
  height: 200px;
}

li {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px;
}

.plan-info {
  color: #4f5665;
  font-weight: 400;
  width: 100%;
  margin: 0 10px;
  text-align: left;
}

.selected {
  border: 2px solid #f53838;
}
</style>
