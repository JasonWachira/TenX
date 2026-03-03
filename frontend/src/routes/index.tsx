import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({ component: App })

function App() {
  return (
    <main>
      <h1>Welcome to the TenX Hackathon Project</h1>
    </main>
  )
}
