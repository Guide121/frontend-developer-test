<template>
  <div class="header-container">
    <img src="@/assets/logo.png" />

    <nav>
      <button @click="scroll('about')">About</button>
      <button @click="scroll('features')">Features</button>
      <button @click="scroll('pricing')">Pricing</button>
      <button @click="scroll('testimonials')">Testimonials</button>
      <button @click="scroll('help')">Help</button>
    </nav>

    <div>
      <button class="buttons sign-in">Sign In</button>
      <button class="buttons sign-up">Sign Up</button>
    </div>
  </div>
</template>

<script>
import ScrollTo from 'scroll-animate-to'

export default {
  methods: {
    scroll(id) {
      const element = document.getElementById(id)

      const scroll = new ScrollTo({
        target: element,
        animationFn: 'easeOut',
        duration: 100,
      })

      scroll.scroll()
    },
  },
}
</script>

<style scoped>
.header-container {
  width: 88%;
  margin: 0 auto 40px;
  padding: 25px;
  justify-content: space-between;
  display: flex;
  align-items: center;
}

.header-container div {
  display: flex;
  width: 20%;
  justify-content: center;
  align-items: center;
}

nav {
  width: 50%;
  display: flex;
  padding: 0 30px;
  justify-content: space-around;
}

nav button {
  color: #4f5665;
  background: transparent;
  border: 0;
  font-family: Rubik, sans-serif;
  font-weight: 400;
  font-size: 1rem;
  cursor: pointer;
  outline: none;
  text-decoration: none;
}

nav button:hover {
  text-decoration: underline;
}

.buttons {
  background: transparent;
  font-family: Rubik, sans-serif;
  font-weight: 500;
  width: 100px;
  padding: 10px;
  outline: none;
  cursor: pointer;
}

.sign-in {
  color: #0b132a;
  border: none;
}

.sign-up {
  color: #f53855;
  border: 1px solid #f53855;
  border-radius: 20px;
}
</style>
