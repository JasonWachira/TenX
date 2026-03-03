import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/candidates/$candidatesId')({
  component: RouteComponent,

})

function RouteComponent() {
  const {candidatesId} = Route.useParams()
  return <div className='p-12'>Hello "{candidatesId}"!</div>
}
