<template>
  <div>
    <button
      :class="
        primary && bordered
          ? 'primary bordered'
          : primary && !bordered
          ? 'primary'
          : 'secondary'
      "
      class="button"
    >
      {{ title }}
    </button>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'Button',
    },

    primary: {
      type: Boolean,
      default: false,
    },

    bordered: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style scoped>
.button {
  font-weight: 700;
  font-family: Rubik, sans-serif;
  cursor: pointer;
}

.primary {
  background: #f53838;
  border-radius: 10px;
  width: 200px;
  padding: 15px;
  border: 0;
  color: #fff;
  box-shadow: 0px 10px 20px rgba(245, 56, 56, 0.35);
}

.secondary {
  background: transparent;
  border: 2px solid #f53838;
  color: #f53838;
  border-radius: 20px;
  width: 150px;
  padding: 10px;
}

.bordered {
  padding: 10px;
  width: 150px;
  border-radius: 20px;
}
</style>
