interface StateTypes {
  counter: number;
}

export default {
  increment(state: StateTypes) {
    state.counter++;
  },
  decrement(state: StateTypes) {
    state.counter--;
  }
};
