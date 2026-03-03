import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/candidates/')({
  component: RouteComponent,
})

function RouteComponent() {
  return (
    <div className='grid gap-10'>
      Hello candidates!


<div className='flex'>
      {Array.from({ length: 5 }).map((_, i) => (
        <div key={i}>
          <a className='hover:bg-gray-100 p-2 rounded-md' href={`/candidates/${i + 1}`}>Candidate {i + 1}</a>
        </div>
      ))}
      </div>
    </div>
  )
}
