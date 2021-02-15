<template>
  <div class="header-container">
    <img src="@/assets/logo.png" />

    <nav>
      <NuxtLink to="#">About</NuxtLink>
      <NuxtLink to="#">Features</NuxtLink>
      <NuxtLink to="#">Pricing</NuxtLink>
      <NuxtLink to="#">Testimonials</NuxtLink>
      <NuxtLink to="#">Help</NuxtLink>
    </nav>

    <div>
      <button class="buttons sign-in">Sign In</button>
      <button class="buttons sign-up">Sign Up</button>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.header-container {
  width: 93%;
  margin: 0 auto 40px;
  padding: 25px;
  justify-content: space-between;
  display: flex;
  align-items: center;
}

nav {
  width: 50%;
  display: flex;
  padding: 0 30px;
  justify-content: space-around;
}

nav a {
  color: #4f5665;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

.buttons {
  background: transparent;
  font-family: Rubik, sans-serif;
  font-weight: 500;
  width: 150px;
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
