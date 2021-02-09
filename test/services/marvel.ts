import axios from "axios";

export default axios.create({
  baseURL: "https://gateway.marvel.com/v1/public"
});
