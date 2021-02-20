import { StateProps, EvaluationsProps } from './state'

export default {
  SET_EVALUATIONS(state: StateProps, list: EvaluationsProps[]) {
    state.evaluations = list
  },
}
