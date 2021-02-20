<template>
  <div>
    <div class="info">
      <div>
        <img :src="card.image" class="profile" />
        <div class="name-address">
          <p class="name">{{ card.name }}</p>
          <p class="address">{{ card.city }}</p>
        </div>
      </div>
      <div class="evaluation">
        {{ card.evaluation }}
        <img src="@/assets/star.png" />
      </div>
    </div>

    <p class="comment">
      {{ card.comment }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    index: {
      type: Number,
      default: 0,
    },

    card: {
      type: Object,
      default: () => {},
    },
  },
}
</script>

<style scoped>
.info {
  display: flex;
  padding: 0 20px;
  justify-content: space-between;
  align-items: center;
}

.info div {
  display: flex;
  align-items: center;
}

.info .name-address {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: 10px;
}

.name {
  color: #0b132a;
  font-weight: 500;
}

.address {
  color: #4f5665;
  font-weight: 400;
}

.info img.profile {
  border-radius: 50%;
}

.comment {
  color: #0b132a;
  margin: 10px 0;
  line-height: 25px;
}

.evaluation {
  color: #0b132a;
}

.evaluation img {
  margin: 0 10px;
}
</style>
