import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({ component: App })

function App() {
  return (
    <main className="p-12">
      Hello "Home!"
    </main>
  )
}
