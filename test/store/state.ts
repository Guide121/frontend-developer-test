export interface EvaluationsProps {
  name: string
  address: string
  evaluation: number
  image: string
  comment: string
}

export interface StateProps {
  evaluations: EvaluationsProps[]
}

export default (): StateProps => ({
  evaluations: [],
})
