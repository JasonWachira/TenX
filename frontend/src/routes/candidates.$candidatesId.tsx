import { createFileRoute } from '@tanstack/react-router'
import { BarChart } from '@mui/x-charts/BarChart';

import CandidateCard from '../components/candidates'
export const Route = createFileRoute('/candidates/$candidatesId')({
  component: RouteComponent,
})

function RouteComponent() {
  const { candidatesId } = Route.useParams()
  return(
    <CandidateCard candidateId={candidatesId} />
)
}
