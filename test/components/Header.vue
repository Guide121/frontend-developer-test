<template>
  <div class="header">
    <h1>
      Marvel
    </h1>

    <button class="cart-button">Carrinho</button>
  </div>
</template>

<script></script>

<style>
.header {
  position: absolute;
  top: 0;
  background: #ee403c;
  width: 100%;
  padding: 15px;
  color: white;
  font-family: Marvel;
  font-size: 1.8rem;
  text-transform: uppercase;
  display: flex;
  justify-content: space-between;
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
