<template>
  <div class="header">
    <h1>
      Marvel
    </h1>

    <Cart />
  </div>
</template>

<script></script>

<style>
.header {
  position: absolute;
  top: 0;
  background: #ee403c;
  width: 100%;
  padding: 25px;
  color: white;
  font-family: Marvel;
  font-size: 1.8rem;
  text-transform: uppercase;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-button {
  color: #fff;
  background: transparent;
  border: 0;
  font-size: 1.8rem;
}

.cart-button:hover {
  border: 1px solid #fff;
  cursor: pointer;
}
</style>
