<template>
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
      <li v-if="standard || premium">
        <img src="@/assets/correct2.png" />
        <span class="plan-info">Connect Anyware</span>
      </li>
      <li v-if="premium">
        <img src="@/assets/correct2.png" />
        <span class="plan-info">Get New Features</span>
      </li>
    </ul>

    <Button :bordered="premium" :primary="premium" title="Select" />
  </div>
</template>

<script>
export default {
  props: {
    standard: {
      type: Boolean,
      default: false,
    },

    premium: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style scoped>
.plan {
  width: 25%;
  height: 90vh;
  border-radius: 10px;
  border: 2px solid #dddddd;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  transition: 0.5s;
}

.plan:hover {
  border: 2px solid #f53838;
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
</style>
