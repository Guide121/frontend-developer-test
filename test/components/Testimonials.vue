<template>
  <div id="testimonials" class="main-container testimonials-container">
    <h1 class="title">Trusted by Thousands of Happy Customer</h1>
    <p class="text">
      These are the stories of our customers who have joined us with great
      pleasure when using this crazy feature.
    </p>

    <div id="cards-list" class="cards-list">
      <!-- <div
        v-for="(card, index) in comments"
        :id="index"
        :key="index"
        class="card"
        :class="selected == index && 'selected'"
      > -->
      <!-- <div class="info">
          <div>
            <img src="https://picsum.photos/50/50" class="profile" />
            <div class="name-address">
              <p class="name">{{ card.name }}</p>
              <p class="address">City</p>
            </div>
          </div>
          <div class="evaluation">
            4.5
            <img src="https://picsum.photos/10/10" />
          </div>
        </div>

        <p class="comment">
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium
          fugiat, dolor repellat culpa perferendis ipsam. Optio eaque reiciendis
          modi fuga illo! Sapiente veritatis placeat sequi nemo harum illo
          perferendis iste!"
        </p> -->
      <TestimonialCard
        v-for="(card, index) in comments"
        :id="index"
        :key="index"
        :card="card"
        :index="index"
        class="card"
        :class="selected == index && 'selected'"
      />
      <!-- </div> -->
    </div>
    <div class="buttons">
      <div>
        <button
          v-for="(index, _) in comments.length"
          :key="index"
          :class="selected === index - 1 && 'button-selected'"
          @click="select(index - 1)"
        ></button>
      </div>

      <div class="next-previous">
        <button
          class="previous"
          :disabled="selected === 0"
          @click="previousSelect"
        >
          <img src="@/assets/arrow-left.svg" />
        </button>
        <button
          class="next"
          :disabled="selected === comments.length - 1"
          @click="nextSelect"
        >
          <img src="@/assets/arrow-right.svg" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import ScrollTo from 'scroll-animate-to'

export default {
  data() {
    return {
      selected: 0,
      comments: [
        {
          name: 'Débora',
        },
        {
          name: 'ASQWE',
        },
        {
          name: 'Débora',
        },
        {
          name: 'Débora',
        },
        {
          name: 'Débora',
        },
      ],
    }
  },
  methods: {
    select(id) {
      this.selected = id

      this.scroll(id)
    },

    nextSelect() {
      if (this.selected === this.comments.length) {
        return
      }
      this.selected += 1

      this.scroll(this.selected)
    },

    previousSelect() {
      if (this.selected === 0) {
        return
      }
      this.selected -= 1

      this.scroll(this.selected)
    },

    scroll(id) {
      const cardsList = document.getElementById('cards-list')
      const testimonial = document.getElementById(id)

      const scroll = new ScrollTo({
        container: cardsList,
        target: testimonial,
        axis: 'x',
        animationFn: 'easeOut',
        duration: 100,
      })

      scroll.scroll()
    },
  },
}
</script>

<style scoped>
.title {
  color: #0b132a;
  margin: 0 auto;
  width: 40%;
  text-align: center;
}

.text {
  color: #4f5665;
  margin: 10px auto 70px;
  text-align: center;
  width: 50%;
}

.cards-list {
  margin: 30px 0;
  display: flex;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

.card {
  min-width: 400px;
  border: 2px solid #dddddd;
  border-radius: 10px;
  padding: 10px;
  margin: 0 10px;
}

.selected {
  transition: 0.5s;
  border: 2px solid #f53838;
}

.buttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.buttons button {
  background: #dde0e4;
  border: none;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  margin: 0 5px 30px;
  cursor: pointer;
  outline: none;
  transition: 0.5s;
}

.buttons .next-previous button {
  width: 50px;
  height: 50px;
}

button.previous {
  border: 2px solid #f53838;
  color: #f53838;
  background: transparent;
}

button.next {
  background: #f53838;
  color: #fff;
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.3);
}

button.next:disabled,
button.previous:disabled {
  cursor: auto;
  opacity: 0.6;
}

button.button-selected {
  width: 35px;
  border-radius: 10px;
  background: #f53838;
  animation: activate 1s;
}
</style>
