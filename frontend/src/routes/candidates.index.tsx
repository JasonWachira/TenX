import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/candidates/')({
  component: RouteComponent,
})

function RouteComponent() {
  return (
  <div className='p-12'>
    Hello, pick a candidate!

    {Array.from({ length: 10 }).map((_, i) => (
      <div key={i}>
        <a href={`/candidates/${i + 1}`}>Candidate {i + 1}</a>
      </div>
    ))}
  </div>)
}
