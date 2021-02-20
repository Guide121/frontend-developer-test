import axios from 'axios'

export default {
  getEvaluations({ commit }) {
    axios
      .get('http://localhost:5000')
      .then((res) => commit('SET_EVALUATIONS', res.data))
  },
}
