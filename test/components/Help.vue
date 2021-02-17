<template>
  <div id="help" class="help-container">
    <div class="container main-container">
      <div class="info">
        <img src="@/assets/logo.png" />
        <p class="text">
          <b>LaslesVPN</b> is a private virtual network that has unique features
          and has high security.
        </p>

        <div class="social-medias">
          <a href="https://facebook.com" target="_blank">
            <img src="@/assets/Facebook.png" />
          </a>
          <a href="https://twitter.com" target="_blank">
            <img src="@/assets/Twitter.png" />
          </a>
          <a href="https://instagram.com" target="_blank">
            <img src="@/assets/Instagram.png" />
          </a>
        </div>

        <p class="copy">&copy;2020Lasles<b>VPN</b></p>
      </div>

      <div class="links">
        <ul>
          <li class="title">Product</li>
          <li>Download</li>
          <li>Pricing</li>
          <li>Locations</li>
          <li>Server</li>
          <li>Countries</li>
          <li>Blog</li>
        </ul>

        <ul>
          <li class="title">Engage</li>
          <li>LaslesVPN ?</li>
          <li>FAQ</li>
          <li>Tutorials</li>
          <li>About Us</li>
          <li>Privacy Policy</li>
          <li>Terms of Service</li>
        </ul>

        <ul>
          <li class="title">Earn Money</li>
          <li>Affiliate</li>
          <li>Become Partner</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.help-container {
  margin: -100px 0 50px;
  position: relative;
  z-index: 1;
  height: auto;
  background: #f8f8f8;
}

.container {
  padding-top: 150px;
  display: flex;
}

.text {
  margin: 10px 0;
  color: #4f5665;
  width: 55%;
}

.social-medias {
  width: 20%;
  display: inline;
}

.social-medias button {
  border: none;
  background: transparent;
  border-radius: 50%;
  color: red;
}

.copy {
  color: #afb5c0;
}

.links {
  display: flex;
  width: 50%;
  justify-content: space-between;
}

ul {
  list-style: none;
  padding-left: 0;
}

.title {
  color: #0b132a;
  font-weight: 500;
}

li {
  color: #4f5665;
  margin: 15px 0;
  cursor: pointer;
}
</style>
