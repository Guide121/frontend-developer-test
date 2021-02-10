interface CartProps {
  id: number;
  title: string;
  image: string;
  price: number;
}

export interface StateTypes {
  cart: CartProps[];
  comics: {}[];
}

export default {
  addToCart(state: StateTypes, comic: CartProps) {
    state.cart.push(comic);
  },
  removeFromCart(state: StateTypes, id: number) {
    const foundComic = state.cart.find(comicId => id);

    state.cart.splice(foundComic, 1);
  },

  getComics(state: StateTypes, list: []) {
    state.comics.push(...list);
  }
};
